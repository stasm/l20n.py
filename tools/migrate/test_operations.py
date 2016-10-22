import unittest
import textwrap

from compare_locales.parser import PropertiesParser
from l20n.format.serializer import FTLSerializer
import l20n.format.ast as FTL

from operations import Copy, Replace, Plural


# Nicer indentation for FTL code
def ftl(string):
    return textwrap.dedent(string[1:])


# Mock Source using the collection parsed in setUp.
def Source(collection, key):
    return collection.get(key, None).get_val()


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


class TestReplaceOperation(unittest.TestCase):
    def setUp(self):
        ftl_serializer = FTLSerializer()
        self.serialize = lambda node: ftl_serializer.dumpEntry(node.toJSON())

        # Parse properties into the internal Context.
        self.prop_parser = PropertiesParser()
        self.prop_parser.readContents('''
            hello = Hello, #1!
            welcome = Welcome, #1, to #2!
            first = #1 Bar
            last = Foo #1
        ''')
        # Transform the parsed result which is an iterator into a dict.
        self.props = {ent.get_key(): ent for ent in self.prop_parser}

    def test_replace_one(self):
        msg = FTL.Entity(
            FTL.Identifier('hello'),
            value=Replace(
                Source(self.props, 'hello'),
                {'#1': [FTL.ExternalArgument('username')]}
            )
        )

        self.assertEqual(
            self.serialize(msg),
            'hello = Hello, { $username }!\n'
        )

    def test_replace_two(self):
        msg = FTL.Entity(
            FTL.Identifier('welcome'),
            value=Replace(
                Source(self.props, 'welcome'),
                {'#1': [FTL.ExternalArgument('username')],
                 '#2': [FTL.ExternalArgument('appname')]}
            )
        )

        self.assertEqual(
            self.serialize(msg),
            'welcome = Welcome, { $username }, to { $appname }!\n'
        )

    def test_replace_too_many(self):
        msg = FTL.Entity(
            FTL.Identifier('welcome'),
            value=Replace(
                Source(self.props, 'welcome'),
                {'#1': [FTL.ExternalArgument('username')],
                 '#2': [FTL.ExternalArgument('appname')],
                 '#3': [FTL.ExternalArgument('extraname')]}
            )
        )

        self.assertEqual(
            self.serialize(msg),
            'welcome = Welcome, { $username }, to { $appname }!\n'
        )

    def test_replace_too_few(self):
        msg = FTL.Entity(
            FTL.Identifier('welcome'),
            value=Replace(
                Source(self.props, 'welcome'),
                {'#1': [FTL.ExternalArgument('username')]}
            )
        )

        self.assertEqual(
            self.serialize(msg),
            'welcome = Welcome, { $username }, to #2!\n'
        )

    def test_replace_first(self):
        msg = FTL.Entity(
            FTL.Identifier('first'),
            value=Replace(
                Source(self.props, 'first'),
                {'#1': [FTL.ExternalArgument('foo')]}
            )
        )

        self.assertEqual(
            self.serialize(msg),
            'first = { $foo } Bar\n'
        )

    def test_replace_last(self):
        msg = FTL.Entity(
            FTL.Identifier('last'),
            value=Replace(
                Source(self.props, 'last'),
                {'#1': [FTL.ExternalArgument('bar')]}
            )
        )

        self.assertEqual(
            self.serialize(msg),
            'last = Foo { $bar }\n'
        )


class TestPluralOperation(unittest.TestCase):
    def setUp(self):
        ftl_serializer = FTLSerializer()
        self.serialize = lambda node: ftl_serializer.dumpEntry(node.toJSON())

        # Parse properties into the internal Context.
        self.prop_parser = PropertiesParser()
        self.prop_parser.readContents('''
            deleteAll=Delete this download?;Delete all downloads?
        ''')
        # Transform the parsed result which is an iterator into a dict.
        self.props = {ent.get_key(): ent for ent in self.prop_parser}

    def test_plural(self):
        msg = FTL.Entity(
            FTL.Identifier('delete-all'),
            value=Plural(
                Source(self.props, 'deleteAll'),
                FTL.ExternalArgument('num'),
                lambda var: Copy(var)
            )
        )

        self.assertEqual(
            self.serialize(msg),
            ftl('''
                delete-all = { $num ->
                  [one] Delete this download?
                 *[other] Delete all downloads?
                }
            ''')
        )


if __name__ == '__main__':
    unittest.main()
