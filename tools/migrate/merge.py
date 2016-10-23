# coding=utf8

import l20n.format.ast as FTL


def get_entity(body, ident):
    """Get entity called `ident` from `body`."""
    for entity in body:
        if entity.id.name == ident:
            return entity


def merge(reference, localization, legacy, transforms):
    """Transform legacy translations into FTL.

    Use the `reference` FTL AST as a template.  For each en-US string in the
    reference, check for an existing translation in the current FTL
    `localization` or for a migration specification in `transforms`.
    """

    def merge_entry(entry):
        ident = entry.id.name

        existing = get_entity(localization.body, ident)
        if existing is not None:
            return existing

        transform = get_entity(transforms, ident)
        if transform is not None:
            return transform

    body = [
        entry for entry in map(merge_entry, reference.body)
        if entry is not None
    ]

    return FTL.Resource(body, reference.comment)
