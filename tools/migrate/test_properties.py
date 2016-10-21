import unittest

from compare_locales.parser import PropertiesParser
from l20n.format.serializer import FTLSerializer
import l20n.format.ast as FTL

from operations import Copy


# Mock Source using the collection parsed in setUp.
def Source(collection, key):
    return collection.get(key, None)


class TestCopyOperation(unittest.TestCase):
    def setUp(self):
        ftl_serializer = FTLSerializer()
        self.serialize = lambda node: ftl_serializer.dumpEntry(node.toJSON())

        # Parse properties into the internal Context.
        self.prop_parser = PropertiesParser()
        self.prop_parser.readContents('''
            foo = Foo
            foo.unicode.middle = Foo\\u0020Bar
            foo.unicode.begin = \\u0020Foo
            foo.unicode.end = Foo\\u0020

            foo.html.entity = &lt;&#x21E7;&#x2318;K&gt;
        ''')
        # Transform the parsed result which is an iterator into a dict.
        self.props = {ent.get_key(): ent for ent in self.prop_parser}

    def test_copy(self):
        msg = FTL.Entity(
            FTL.Identifier('foo'),
            value=Copy(
                Source(self.props, 'foo')
            )
        )

        self.assertEqual(
            self.serialize(msg),
            'foo = Foo\n'
        )

    def test_copy_escape_unicode_middle(self):
        msg = FTL.Entity(
            FTL.Identifier('foo-unicode-middle'),
            value=Copy(
                Source(self.props, 'foo.unicode.middle')
            )
        )

        self.assertEqual(
            self.serialize(msg),
            'foo-unicode-middle = Foo Bar\n'
        )

    def test_copy_escape_unicode_begin(self):
        msg = FTL.Entity(
            FTL.Identifier('foo-unicode-begin'),
            value=Copy(
                Source(self.props, 'foo.unicode.begin')
            )
        )

        self.assertEqual(
            self.serialize(msg),
            'foo-unicode-begin = " Foo"\n'
        )

    def test_copy_escape_unicode_end(self):
        msg = FTL.Entity(
            FTL.Identifier('foo-unicode-end'),
            value=Copy(
                Source(self.props, 'foo.unicode.end')
            )
        )

        self.assertEqual(
            self.serialize(msg),
            'foo-unicode-end = "Foo "\n'
        )

    def test_copy_html_entity(self):
        msg = FTL.Entity(
            FTL.Identifier('foo-html-entity'),
            value=Copy(
                Source(self.props, 'foo.html.entity')
            )
        )

        self.assertEqual(
            self.serialize(msg),
            'foo-html-entity = &lt;&#x21E7;&#x2318;K&gt;\n'
        )


if __name__ == '__main__':
    unittest.main()
