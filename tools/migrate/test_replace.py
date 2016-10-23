# coding=utf8

import unittest

import l20n.format.ast as FTL
from compare_locales.parser import PropertiesParser
from util import parse, dumpEntry, ftl

from operations import REPLACE


# Mock SOURCE using the collection parsed in setUp.
def SOURCE(collection, key):
    return collection.get(key, None).get_val()


class TestReplace(unittest.TestCase):
    def setUp(self):
        self.strings = parse(PropertiesParser, '''
            hello = Hello, #1!
            welcome = Welcome, #1, to #2!
            first = #1 Bar
            last = Foo #1
        ''')

    def test_replace_one(self):
        msg = FTL.Entity(
            FTL.Identifier('hello'),
            value=REPLACE(
                SOURCE(self.strings, 'hello'),
                {'#1': [FTL.ExternalArgument('username')]}
            )
        )

        self.assertEqual(
            dumpEntry(msg),
            ftl('''
                hello = Hello, { $username }!
            ''')
        )

    def test_replace_two(self):
        msg = FTL.Entity(
            FTL.Identifier('welcome'),
            value=REPLACE(
                SOURCE(self.strings, 'welcome'),
                {'#1': [FTL.ExternalArgument('username')],
                 '#2': [FTL.ExternalArgument('appname')]}
            )
        )

        self.assertEqual(
            dumpEntry(msg),
            ftl('''
                welcome = Welcome, { $username }, to { $appname }!
            ''')
        )

    def test_replace_too_many(self):
        msg = FTL.Entity(
            FTL.Identifier('welcome'),
            value=REPLACE(
                SOURCE(self.strings, 'welcome'),
                {'#1': [FTL.ExternalArgument('username')],
                 '#2': [FTL.ExternalArgument('appname')],
                 '#3': [FTL.ExternalArgument('extraname')]}
            )
        )

        self.assertEqual(
            dumpEntry(msg),
            ftl('''
                welcome = Welcome, { $username }, to { $appname }!
            ''')
        )

    def test_replace_too_few(self):
        msg = FTL.Entity(
            FTL.Identifier('welcome'),
            value=REPLACE(
                SOURCE(self.strings, 'welcome'),
                {'#1': [FTL.ExternalArgument('username')]}
            )
        )

        self.assertEqual(
            dumpEntry(msg),
            ftl('''
                welcome = Welcome, { $username }, to #2!
            ''')
        )

    def test_replace_first(self):
        msg = FTL.Entity(
            FTL.Identifier('first'),
            value=REPLACE(
                SOURCE(self.strings, 'first'),
                {'#1': [FTL.ExternalArgument('foo')]}
            )
        )

        self.assertEqual(
            dumpEntry(msg),
            ftl('''
                first = { $foo } Bar
            ''')
        )

    def test_replace_last(self):
        msg = FTL.Entity(
            FTL.Identifier('last'),
            value=REPLACE(
                SOURCE(self.strings, 'last'),
                {'#1': [FTL.ExternalArgument('bar')]}
            )
        )

        self.assertEqual(
            dumpEntry(msg),
            ftl('''
                last = Foo { $bar }
            ''')
        )


if __name__ == '__main__':
    unittest.main()
