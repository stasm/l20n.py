# coding=utf8

import os
import codecs
import logging

import l20n.format.ast as FTL
from l20n.format.parser import FTLParser
from l20n.format.serializer import FTLSerializer
from compare_locales.parser import getParser

from cldr import get_plural_categories
from operations import VARIANTS


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


class MergeContext(object):
    """Stateful context for merging translation resources.

    `MergeContext` must be configured with the target language and the
    directory locations of the input data.

    The transformation takes four types of input data:

        - The en-US FTL reference files which will be used as templates for
          message order, comments and sections.

        - The current FTL files for the given language.

        - The legacy (DTD, properties) translation files for the given
          language.  The translations from these files will be transformed
          into FTL and merged into the existing FTL files for this language.

        - A list of `FTL.Entity` objects whose some nodes are special operation
          nodes: COPY, REPLACE, PLURALS, CONCAT, INTERPOLATE.
    """

    def __init__(self, lang, reference_dir, localization_dir):
        self.ftl_parser = FTLParser()
        self.ftl_serializer = FTLSerializer()

        # An iterable of plural category names relevant to the context's
        # language.  E.g. ('one', 'other') for English.
        self.plural_categories = get_plural_categories(lang)

        # Paths to directories with input data, relative to CWD.
        self.reference_dir = reference_dir
        self.localization_dir = localization_dir

        # Parsed input resources stored by resource path.
        self.reference_resources = {}
        self.current_resources = {}
        self.legacy_resources = {}

        # An iterable of `FTL.Entity` object whose some nodes can be the
        # transform operations: COPY, REPLACE, PLURALS, CONCAT, INTERPOLATE.
        self.transforms = {}

    def read_ftl_resource(self, path):
        f = codecs.open(path, 'r', 'utf8')
        try:
            contents = f.read()
        except UnicodeDecodeError, err:
            logger = logging.getLogger('migrate')
            logger.error(u'Error reading file {}: {}'.format(path, str(err)))
        f.close()

        ast, errors = self.ftl_parser.parse(contents)

        if len(errors):
            logger = logging.getLogger('migrate')
            for err in errors:
                logger.error(u'Syntax error in {}: {}'.format(path, str(err)))

        return ast

    def add_reference(self, path):
        """Add an FTL AST to this context's reference resources."""
        fullpath = os.path.join(self.reference_dir, path)
        self.reference_resources[path] = self.read_ftl_resource(fullpath)

    def add_current(self, path):
        """Add an FTL AST to this context's current localization resources."""
        fullpath = os.path.join(self.localization_dir, path)
        self.current_resources[path] = self.read_ftl_resource(fullpath)

    def add_legacy(self, path):
        """Add a dict to this context's legacy localization resources."""
        fullpath = os.path.join(self.localization_dir, path)
        parser = getParser(fullpath)
        parser.readFile(fullpath)
        # Transform the parsed result which is an iterator into a dict.
        collection = {ent.get_key(): ent for ent in parser}
        self.legacy_resources[path] = collection

    def add_transforms(self, path, transforms):
        """Define transforms for `path`."""
        self.transforms[path] = transforms

    def create_source(self):
        """Create a SOURCE partial for use with other operations."""
        def source(path, key):
            entity = self.legacy_resources[path].get(key, None)
            if entity is not None:
                return entity.get_val()
        return source

    def create_plurals(self):
        """Create a PLURALS partial for use with other operations."""
        def plurals(source, selector, foreach):
            return VARIANTS(source, selector, self.plural_categories, foreach)
        return plurals

    def merge(self, changeset):
        """Transform and merge context's input data.

        The input data must be configured earlier using the `add_*` methods.
        The `changeset` argument is a dict of (file path, list of keys)
        describing which legacy traslations should be transformed.
        """

        # XXX Filter legacy_resources according to changeset.
        changed = self.legacy_resources

        result = {}

        for path, reference in self.reference_resources.iteritems():
            current = self.current_resources.get(path, FTL.Resource())
            transforms = self.transforms.get(path, [])

            merged = merge(reference, current, changed, transforms)
            result[path] = self.ftl_serializer.serialize(merged.toJSON())

        return result
