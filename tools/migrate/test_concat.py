# coding=utf8

import unittest

import l20n.format.ast as FTL
from compare_locales.parser import PropertiesParser, DTDParser
from util import parse, dumpEntry, ftl

from operations import COPY, INTERPOLATE, REPLACE, CONCAT


# Mock SOURCE using the collection parsed in setUp.
def SOURCE(collection, key):
    return collection.get(key, None).get_val()


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
            dumpEntry(msg),
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
            len(msg.value.elements),
            1,
            'The constructed value should have only one element'
        )
        self.assertIsInstance(
            msg.value.elements[0],
            FTL.TextElement,
            'The constructed element should be a TextElement.'
        )
        self.assertEqual(
            msg.value.elements[0].value,
            'Hello, world!',
            'The TextElement should be a concatenation of the sources.'
        )

        self.assertEqual(
            dumpEntry(msg),
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
            dumpEntry(msg),
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
            dumpEntry(msg),
            ftl('''
                hello = "Hello, world! "
            ''')
        )


class TestConcatLiteral(unittest.TestCase):
    def setUp(self):
        self.strings = parse(DTDParser, '''
            <!ENTITY update.failed.start        "Update failed. ">
            <!ENTITY update.failed.linkText     "Download manually">
            <!ENTITY update.failed.end          "!">
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
            dumpEntry(msg),
            ftl('''
                update-failed = Update failed. <a>Download manually</a>!
            ''')
        )


class TestConcatInterpolate(unittest.TestCase):
    def setUp(self):
        self.strings = parse(DTDParser, '''
            <!ENTITY channel.description.start  "You are on the ">
            <!ENTITY channel.description.end    " channel. ">
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
            dumpEntry(msg),
            ftl('''
                channel-desc = "You are on the { $channelname } channel. "
            ''')
        )


class TestConcatReplace(unittest.TestCase):
    def setUp(self):
        self.strings = parse(DTDParser, '''
            <!ENTITY community.start       "&brandShortName; is designed by ">
            <!ENTITY community.mozillaLink "&vendorShortName;">
            <!ENTITY community.middle      ", a ">
            <!ENTITY community.creditsLink "global community">
            <!ENTITY community.end         " working together to…">
        ''')

    def test_concat_replace(self):
        msg = FTL.Entity(
            FTL.Identifier('community'),
            value=CONCAT(
                REPLACE(
                    SOURCE(self.strings, 'community.start'),
                    {
                        '&brandShortName;': [
                            FTL.ExternalArgument('brand-short-name')
                        ]
                    }
                ),
                COPY('<a>'),
                REPLACE(
                    SOURCE(self.strings, 'community.mozillaLink'),
                    {
                        '&vendorShortName;': [
                            FTL.ExternalArgument('vendor-short-name')
                        ]
                    }
                ),
                COPY('</a>'),
                COPY(
                    SOURCE(self.strings, 'community.middle')
                ),
                COPY('<a>'),
                COPY(
                    SOURCE(self.strings, 'community.creditsLink')
                ),
                COPY('</a>'),
                COPY(
                    SOURCE(self.strings, 'community.end')
                )
            )
        )

        self.assertEqual(
            dumpEntry(msg),
            ftl('community = { $brand-short-name } is designed by '
                '<a>{ $vendor-short-name }</a>, a <a>global community</a> '
                'working together to…')
        )


if __name__ == '__main__':
    unittest.main()
