# coding=utf8

import os
import codecs
import logging

import l20n.format.ast as FTL
from l20n.format.parser import FTLParser
from l20n.format.serializer import FTLSerializer
from compare_locales.parser import getParser

from cldr import get_plural_categories
from transforms import SOURCE
from merge import merge_resource
from util import get_entity, fold_ftl


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
          nodes: CONCAT, COPY, EXTERNAL, PLURALS, REPLACE, SOURCE.
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
        self.localization_resources = {}

        # An iterable of `FTL.Entity` objects whose some nodes can be the
        # transform operations.
        self.transforms = {}

        # A dict whose keys are `(path, key)` tuples corresponding to target
        # FTL translations, and values are sets of `(path, key)` tuples
        # corresponding to localized entities which will be migrated.
        self.dependencies = {}

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

    def add_reference(self, path, realpath=None):
        """Add an FTL AST to this context's reference resources."""
        fullpath = os.path.join(self.reference_dir, realpath or path)
        self.reference_resources[path] = self.read_ftl_resource(fullpath)

    def add_localization(self, path):
        """Add an existing localization resource.

        If it's an FTL resource, add an FTL AST.  Otherwise, it's a legacy
        resource.  Use a compare-locales parser to create a dict of (key,
        string value) tuples.
        """
        fullpath = os.path.join(self.localization_dir, path)
        if fullpath.endswith('.ftl'):
            ast = self.read_ftl_resource(fullpath)
            self.localization_resources[path] = ast
        else:
            parser = getParser(fullpath)
            parser.readFile(fullpath)
            # Transform the parsed result which is an iterator into a dict.
            collection = {ent.get_key(): ent for ent in parser}
            self.localization_resources[path] = collection

    def add_transforms(self, path, transforms):
        """Define transforms for path.

        Each transform is an extended FTL node with `Transform` nodes as some
        values.  Transforms are stored in their lazy AST form until
        `merge_changeset` is called, at which point they are evaluated to real
        FTL nodes with migrated translations.

        Each transform is scanned for `SOURCE` nodes which will be used to
        build the list of dependencies for the transformed message.
        """
        def get_sources(acc, cur):
            if isinstance(cur, SOURCE):
                acc.add((cur.path, cur.key))
            return acc

        for node in transforms:
            # Scan `node` for `SOURCE` nodes and collect the information they
            # store into a set of dependencies.
            dependencies = fold_ftl(get_sources, node, set())
            # Set this source as a dependency for the current transform.
            self.dependencies[(path, node.id.name)] = dependencies

        path_transforms = self.transforms.setdefault(path, [])
        path_transforms.extend(transforms)

    def get_source(self, path, key):
        """Get an entity from the localized source.

        Used by the `SOURCE` transform.
        """
        if path.endswith('.ftl'):
            resource = self.localization_resources[path]
            return get_entity(resource.entities(), key)
        else:
            resource = self.localization_resources[path]
            entity = resource.get(key, None)
            if entity is not None:
                return entity.get_val()

    def merge_changeset(self, changeset=None):
        """Return a generator of FTL ASTs for the changeset.

        The input data must be configured earlier using the `add_*` methods.
        if given, `changeset` must be a set of (path, key) tuples describing
        which legacy translations are to be merged.

        Given `changeset`, return a dict whose keys are resource paths and
        values are `FTL.Resource` instances.  The values will also be used to
        update this context's existing localization resources.
        """

        if changeset is None:
            # Merge all known legacy translations.
            changeset = {
                (path, key)
                for path, strings in self.localization_resources.iteritems()
                for key in strings.iterkeys()
                if not path.endswith('.ftl')
            }

        for path, reference in self.reference_resources.iteritems():
            current = self.localization_resources.get(path, FTL.Resource())
            transforms = self.transforms.get(path, [])

            def in_changeset(ident):
                """Check if entity should be merged.

                If at least one dependency of the entity is in the current
                set of changeset, merge it.
                """
                message_deps = self.dependencies.get((path, ident), set())
                # Take the intersection of dependencies and the changeset.
                return message_deps & changeset

            # Merge legacy translations with the existing ones using the
            # reference as a template.
            snapshot = merge_resource(
                self, reference, current, transforms, in_changeset
            )

            # If none of the transforms is in the given changeset, the merged
            # snapshot is identical to the current translation. We compare
            # JSON trees rather then use filtering by `in_changeset` to account
            # for translations removed from `reference`.
            if snapshot.toJSON() == current.toJSON():
                continue

            # Store the merged snapshot on the context so that the next merge
            # already takes it into account as the existing localization.
            self.localization_resources[path] = snapshot

            # The result for this path is a complete `FTL.Resource`.
            yield path, snapshot

    def serialize_changeset(self, changeset):
        """Return a dict of serialized FTLs for the changeset.

        Given `changeset`, return a dict whose keys are resource paths and
        values are serialized FTL snapshots.
        """

        return {
            path: self.ftl_serializer.serialize(snapshot.toJSON())
            for path, snapshot in self.merge_changeset(changeset)
        }
