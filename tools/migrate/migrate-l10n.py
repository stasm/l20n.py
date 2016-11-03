# coding=utf8

import os
import json
import argparse
import importlib

import hglib
from hglib.util import b

from l20n.migrate import MergeContext, convert_blame_to_changesets


def main(lang, reference_dir, localization_dir, blame, migrations):
    """Run migrations and commit files with the result."""
    changesets = convert_blame_to_changesets(blame)
    client = hglib.open(localization_dir)

    for migration in migrations:

        print('Running migration {}'.format(migration.__name__))

        # For each migration create a new context.
        ctx = MergeContext(lang, reference_dir, localization_dir)

        # Add the migration spec.
        migration.migrate(ctx)

        # Keep track of how many changesets we're committing.
        index = 0

        for changeset in changesets:
            # Run the migration.
            snapshot = ctx.serialize_changeset(changeset['changes'])

            # The current changeset didn't touch any of the translations
            # affected by the migration.
            if not snapshot:
                continue

            # Write serialized FTL files to disk.
            for path, content in snapshot.iteritems():
                fullpath = os.path.join(localization_dir, path)
                with open(fullpath, 'w') as f:
                    print('  Writing to {}'.format(fullpath))
                    f.write(content.encode('utf8'))
                    f.close()

            index += 1
            message = migration.migrate.__doc__.format(
                index=index,
                author=changeset['author'],
                files='\n'.join(snapshot.keys())
            )

            print('    Committing changeset: {}'.format(message))
            client.commit(
                b(message), user=b(changeset['author']), addremove=True
            )

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Migrate translations to FTL.'
    )
    parser.add_argument(
        'migrations', metavar='MIGRATION', type=str, nargs='+',
        help='migrations to run (Python modules)'
    )
    parser.add_argument(
        '--lang', type=str,
        help='target language code'
    )
    parser.add_argument(
        '--source-base', type=str,
        help='directory base with source FTL files'
    )
    parser.add_argument(
        '--l10n-base', type=str,
        help='directory base for localization files'
    )
    parser.add_argument(
        '--blame', type=argparse.FileType(),
        help='path to a JSON with blame information'
    )

    args = parser.parse_args()

    # Be nice to shell autocomplete and allow specifying the full name of each
    # migration module file, including the .py extension.
    module_names = [
        name.rstrip('.py') for name in args.migrations
    ]

    main(
        lang=args.lang,
        reference_dir=args.source_base,
        localization_dir=args.l10n_base,
        blame=json.load(args.blame),
        migrations=map(importlib.import_module, module_names)
    )
