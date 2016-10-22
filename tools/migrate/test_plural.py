# coding=utf8

import unittest

import l20n.format.ast as FTL
from compare_locales.parser import PropertiesParser
from util import parse, serialize, ftl

from operations import COPY, REPLACE, PLURAL


# Mock SOURCE using the collection parsed in setUp.
def SOURCE(collection, key):
    return collection.get(key, None).get_val()


class TestPlural(unittest.TestCase):
    def setUp(self):
        self.strings = parse(PropertiesParser, '''
            deleteAll=Delete this download?;Delete all downloads?
        ''')

    def test_plural(self):
        msg = FTL.Entity(
            FTL.Identifier('delete-all'),
            value=PLURAL(
                SOURCE(self.strings, 'deleteAll'),
                FTL.ExternalArgument('num'),
                lambda var: COPY(var)
            )
        )

        self.assertEqual(
            serialize(msg),
            ftl('''
                delete-all = { $num ->
                  [one] Delete this download?
                 *[other] Delete all downloads?
                }
            ''')
        )


class TestPluralReplace(unittest.TestCase):
    def setUp(self):
        self.strings = parse(PropertiesParser, '''
            deleteAll=Delete this download?;Delete #1 downloads?
        ''')

    def test_plural_replace(self):
        msg = FTL.Entity(
            FTL.Identifier('delete-all'),
            value=PLURAL(
                SOURCE(self.strings, 'deleteAll'),
                FTL.ExternalArgument('num'),
                lambda var: REPLACE(
                    var,
                    {'#1': [FTL.ExternalArgument('num')]}
                )
            )
        )

        self.assertEqual(
            serialize(msg),
            ftl('''
                delete-all = { $num ->
                  [one] Delete this download?
                 *[other] Delete { $num } downloads?
                }
            ''')
        )


if __name__ == '__main__':
    unittest.main()
