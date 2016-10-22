# coding=utf8

import unittest

import l20n.format.ast as FTL
from compare_locales.parser import PropertiesParser
from util import parse, serialize, ftl

from operations import COPY


# Mock SOURCE using the collection parsed in setUp.
def SOURCE(collection, key):
    return collection.get(key, None).get_val()


class TestCopy(unittest.TestCase):
    def setUp(self):
        self.strings = parse(PropertiesParser, '''
            foo = Foo
            foo.unicode.middle = Foo\\u0020Bar
            foo.unicode.begin = \\u0020Foo
            foo.unicode.end = Foo\\u0020

            foo.html.entity = &lt;&#x21E7;&#x2318;K&gt;
        ''')

    def test_copy(self):
        msg = FTL.Entity(
            FTL.Identifier('foo'),
            value=COPY(
                SOURCE(self.strings, 'foo')
            )
        )

        self.assertEqual(
            serialize(msg),
            ftl('''
                foo = Foo
            ''')
        )

    def test_copy_escape_unicode_middle(self):
        msg = FTL.Entity(
            FTL.Identifier('foo-unicode-middle'),
            value=COPY(
                SOURCE(self.strings, 'foo.unicode.middle')
            )
        )

        self.assertEqual(
            serialize(msg),
            ftl('''
                foo-unicode-middle = Foo Bar
            ''')
        )

    def test_copy_escape_unicode_begin(self):
        msg = FTL.Entity(
            FTL.Identifier('foo-unicode-begin'),
            value=COPY(
                SOURCE(self.strings, 'foo.unicode.begin')
            )
        )

        self.assertEqual(
            serialize(msg),
            ftl('''
                foo-unicode-begin = " Foo"
            ''')
        )

    def test_copy_escape_unicode_end(self):
        msg = FTL.Entity(
            FTL.Identifier('foo-unicode-end'),
            value=COPY(
                SOURCE(self.strings, 'foo.unicode.end')
            )
        )

        self.assertEqual(
            serialize(msg),
            ftl('''
                foo-unicode-end = "Foo "
            ''')
        )

    def test_copy_html_entity(self):
        msg = FTL.Entity(
            FTL.Identifier('foo-html-entity'),
            value=COPY(
                SOURCE(self.strings, 'foo.html.entity')
            )
        )

        self.assertEqual(
            serialize(msg),
            ftl('''
                foo-html-entity = &lt;&#x21E7;&#x2318;K&gt;
            ''')
        )


if __name__ == '__main__':
    unittest.main()
