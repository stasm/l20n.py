import l20n.format.ast as FTL


def Copy(source):
    """Copy the translation value from the given source.

    The translation must be a simple value without interpolations nor plural
    variants.  All \uXXXX will be converted to the literal characters they
    encode.

    HTML entities are left unchanged for now.  They're use might or might not
    be intentional.  Consider the following example in which `&amp;` could be
    replaced with the literal `&`:

        Privacy &amp; History

    vs. these two examples where the HTML encoding should be preserved:

        Erreur&nbsp;!
        Use /help &lt;command&gt; for more information.

    """
    # XXX Perhaps there's a strict subset of HTML entities which must or must
    # not be replaced?

    # Entity.get_val() returns already parsed characters for \uXXXX encodings.
    text = source.get_val()

    return FTL.Pattern(
        None,
        [FTL.TextElement(text)],
        quoteDelim=text.startswith(' ') or text.endswith(' ')
    )


def Replace(source, repls):
    """Replace various placeables in the translation with FTL placeables.

    The original placeables are defined as keys on the `repls` dict.  For each
    key the value is defined as a list of FTL Expressions to be interpolated.
    """

    text = source.get_val()
    # Only replace placeable which are present in the translation.
    repls = {k: v for k, v in repls.iteritems() if k in text}
    # Order the original placeables by their position in the translation.
    keys_in_order = sorted(
        repls.keys(),
        lambda x, y: text.find(x) - text.find(y)
    )

    # Used to reduce the `keys_in_order` list.
    def replace(acc, cur):
        """Convert original placeables and text into FTL Nodes.

        For each original placeable the translation will be partitioned around
        it and the text before it will be converted into an `FTL.TextElement`
        and the placeable will be converted to an `FTL.Placeable`. The text
        following the placebale will be fed again to the `replace` function.
        """
        parts, rest = acc
        before, sep, after = rest.value.partition(cur)
        text_before = FTL.TextElement(before)
        placeable = FTL.Placeable(repls[sep])
        text_after = FTL.TextElement(after)
        # Return the elemets found and converted so far, and the remaining text
        # which hasn't been scanned for placeables yet.
        return parts + [text_before, placeable], text_after

    # Start with an empty list of elements and the original translation. It's
    # wrapped in `FTL.TextElement` here to transparently work with `replace`.
    init = ([], FTL.TextElement(text))
    parts, tail = reduce(replace, keys_in_order, init)
    # We need to explicitly concat the trailing text to get the full list of
    # elements.
    elements = parts + [tail]

    return FTL.Pattern(
        None,
        elements,
        quoteDelim=text.startswith(' ') or text.endswith(' ')
    )
