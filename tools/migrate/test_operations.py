import unittest
import textwrap

from compare_locales.parser import PropertiesParser
from l20n.format.serializer import FTLSerializer
import l20n.format.ast as FTL

from operations import COPY, INTERPOLATE, REPLACE, PLURAL, CONCAT


ftl_serializer = FTLSerializer()


def ftl(string):
    """Nicer indentation for FTL code."""
    return textwrap.dedent(string[1:])


def serialize(node):
    return ftl_serializer.dumpEntry(node.toJSON())


def parse(Parser, string):
    # Parse the string into the internal Context.
    parser = Parser()
    parser.readContents(string)
    # Transform the parsed result which is an iterator into a dict.
    return {ent.get_key(): ent for ent in parser}


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
            'foo = Foo\n'
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
            'foo-unicode-middle = Foo Bar\n'
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
            'foo-unicode-begin = " Foo"\n'
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
            'foo-unicode-end = "Foo "\n'
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
            'foo-html-entity = &lt;&#x21E7;&#x2318;K&gt;\n'
        )


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
            serialize(msg),
            'hello = Hello, { $username }!\n'
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
            serialize(msg),
            'welcome = Welcome, { $username }, to { $appname }!\n'
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
            serialize(msg),
            'welcome = Welcome, { $username }, to { $appname }!\n'
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
            serialize(msg),
            'welcome = Welcome, { $username }, to #2!\n'
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
            serialize(msg),
            'first = { $foo } Bar\n'
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
            serialize(msg),
            'last = Foo { $bar }\n'
        )


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


class TestConcatCopy(unittest.TestCase):
    def setUp(self):
        self.strings = parse(PropertiesParser, '''
            hello = Hello, world!
            hello.start = Hello,\\u0020
            hello.end = world!
            whitespace.begin.start = \\u0020Hello,\\u0020
            whitespace.begin.end = world!
            whitespace.end.start = Hello,\\u0020
            whitespace.end.end = world!\\u0020
        ''')

    def test_concat_one(self):
        msg = FTL.Entity(
            FTL.Identifier('hello'),
            value=CONCAT(
                COPY(
                    SOURCE(self.strings, 'hello'),
                ),
            )
        )

        self.assertEqual(
            serialize(msg),
            ftl('''
                hello = Hello, world!
            ''')
        )

    def test_concat_two(self):
        msg = FTL.Entity(
            FTL.Identifier('hello'),
            value=CONCAT(
                COPY(
                    SOURCE(self.strings, 'hello.start'),
                ),
                COPY(
                    SOURCE(self.strings, 'hello.end'),
                )
            )
        )

        self.assertEqual(
            serialize(msg),
            ftl('''
                hello = Hello, world!
            ''')
        )

    def test_concat_whitespace_begin(self):
        msg = FTL.Entity(
            FTL.Identifier('hello'),
            value=CONCAT(
                COPY(
                    SOURCE(self.strings, 'whitespace.begin.start'),
                ),
                COPY(
                    SOURCE(self.strings, 'whitespace.begin.end'),
                )
            )
        )

        self.assertEqual(
            serialize(msg),
            ftl('''
                hello = " Hello, world!"
            ''')
        )

    def test_concat_whitespace_end(self):
        msg = FTL.Entity(
            FTL.Identifier('hello'),
            value=CONCAT(
                COPY(
                    SOURCE(self.strings, 'whitespace.end.start'),
                ),
                COPY(
                    SOURCE(self.strings, 'whitespace.end.end'),
                )
            )
        )

        self.assertEqual(
            serialize(msg),
            ftl('''
                hello = "Hello, world! "
            ''')
        )


class TestConcatLiteral(unittest.TestCase):
    def setUp(self):
        self.strings = parse(PropertiesParser, '''
            update.failed.start    = Update failed.\\u0020
            update.failed.linkText = Download manually
            update.failed.end      = !
        ''')

    def test_concat_literal(self):
        msg = FTL.Entity(
            FTL.Identifier('update-failed'),
            value=CONCAT(
                COPY(
                    SOURCE(self.strings, 'update.failed.start'),
                ),
                COPY('<a>'),
                COPY(
                    SOURCE(self.strings, 'update.failed.linkText'),
                ),
                COPY('</a>'),
                COPY(
                    SOURCE(self.strings, 'update.failed.end'),
                ),
            )
        )

        self.assertEqual(
            serialize(msg),
            ftl('''
                update-failed = Update failed. <a>Download manually</a>!
            ''')
        )


class TestConcatInterpolate(unittest.TestCase):
    def setUp(self):
        self.strings = parse(PropertiesParser, '''
            channel.description.start = You are on the\\u0020
            channel.description.end   = \\u0020channel.\\u0020
        ''')

    def test_concat_replace(self):
        msg = FTL.Entity(
            FTL.Identifier('channel-desc'),
            value=CONCAT(
                COPY(
                    SOURCE(self.strings, 'channel.description.start'),
                ),
                INTERPOLATE('channelname'),
                COPY(
                    SOURCE(self.strings, 'channel.description.end'),
                )
            )
        )

        self.assertEqual(
            serialize(msg),
            ftl('''
                channel-desc = "You are on the { $channelname } channel. "
            ''')
        )


if __name__ == '__main__':
    unittest.main()
