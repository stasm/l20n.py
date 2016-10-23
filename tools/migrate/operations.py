import l20n.format.ast as FTL


def COPY(source):
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

    return FTL.Pattern(
        None,
        [FTL.TextElement(source)],
        quoteDelim=source.startswith(' ') or source.endswith(' ')
    )


def INTERPOLATE(name):
    """Create an FTL placeable with the external argument `name`

    This is a common use-case when joining translations with CONCAT.
    """
    external = FTL.ExternalArgument(name)
    elements = [FTL.Placeable([external])]

    return FTL.Pattern(
        None,
        elements,
        quoteDelim=False
    )


def REPLACE(source, repls):
    """Replace various placeables in the translation with FTL placeables.

    The original placeables are defined as keys on the `repls` dict.  For each
    key the value is defined as a list of FTL Expressions to be interpolated.
    """

    # Only replace placeable which are present in the translation.
    repls = {k: v for k, v in repls.iteritems() if k in source}
    # Order the original placeables by their position in the translation.
    keys_in_order = sorted(
        repls.keys(),
        lambda x, y: source.find(x) - source.find(y)
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

        # Return the elements found and converted so far, and the remaining
        # text which hasn't been scanned for placeables yet.
        return parts + [text_before, placeable], text_after

    # Start with an empty list of elements and the original translation. It's
    # wrapped in `FTL.TextElement` here to transparently work with `replace`.
    init = ([], FTL.TextElement(source))
    parts, tail = reduce(replace, keys_in_order, init)
    # We need to explicitly concat the trailing text to get the full list of
    # elements.
    elements = parts + [tail]

    return FTL.Pattern(
        None,
        elements,
        quoteDelim=source.startswith(' ') or source.endswith(' ')
    )


def VARIANTS(source, selector, keys, foreach):
    """Convert semicolon-separated variants into a select expression.

    Build an `FTL.SelectExpression` with the supplied `selector` and variants
    extracted from the `source`.  Each variant will be run through the
    `foreach` function.  It should return an `FTL.Pattern`.
    """
    variants = source.split(';')
    keys_iter = iter(keys)

    def createMember(variant):
        key = next(keys_iter)
        return FTL.Member(
            FTL.Keyword(key),
            foreach(variant),
            default=key == 'other'
        )

    select = FTL.SelectExpression(
        selector,
        variants=map(createMember, variants)
    )

    elements = [FTL.Placeable([select])]

    return FTL.Pattern(
        None,
        elements,
        quoteDelim=False
    )


def CONCAT(*patterns):
    """Concatenate elements of many patterns."""

    # Flatten the list of patterns of which each has a list of elements.
    elements = [elems for pattern in patterns for elems in pattern.elements]

    # Merge adjecent `FTL.TextElement` nodes.
    def merge_adjecent_text(acc, cur):
        if len(acc) == 0 or type(cur) != FTL.TextElement:
            acc.append(cur)
            return acc

        last = acc[-1]
        if type(last) == FTL.TextElement:
            last.value += cur.value
        else:
            acc.append(cur)
        return acc

    elements = reduce(merge_adjecent_text, elements, [])

    quoteDelim = ((type(elements[0]) is FTL.TextElement and
                   elements[0].value.startswith(' ')) or
                  (type(elements[-1]) is FTL.TextElement and
                   elements[-1].value.endswith(' ')))

    return FTL.Pattern(
        None,
        elements,
        quoteDelim
    )
