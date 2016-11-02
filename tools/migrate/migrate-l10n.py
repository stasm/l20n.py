# coding=utf8

import argparse
import importlib

from l20n.migrate import MergeContext, convert_blame_to_changesets


def main(lang, reference_dir, localization_dir, migrations):
    ctx = MergeContext(
        lang,
        reference_dir,
        localization_dir
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

    args = parser.parse_args()

    module_names = [
        name.rstrip('.py') for name in args.migrations
    ]

    main(
        lang=args.lang,
        reference_dir=args.source_base,
        localization_dir=args.l10n_base,
        migrations=map(importlib.import_module, module_names)
    )
