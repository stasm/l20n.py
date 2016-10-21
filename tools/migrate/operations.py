import l20n.format.ast as FTL


def Copy(source):
    """Copy the translation value from the given source

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
