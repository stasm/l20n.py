# coding=utf8

import unittest

import l20n.format.ast as FTL

from transforms import CONCAT, COPY, SOURCE
from util import ftl_resource_to_ast, fold_ftl


def get_source(acc, cur):
    if isinstance(cur, SOURCE):
        return acc + ((cur.path, cur.key),)
    return acc


class TestMap(unittest.TestCase):
    def test_simple_values(self):
        ast = ftl_resource_to_ast('''
            foo = Foo
            bar = Bar
        ''')

        self.assertEqual(
            ast.map(lambda x: x).toJSON(),
            ast.toJSON()
        )

    def test_complex_values(self):
        ast = ftl_resource_to_ast('''
            foo = Foo { bar }
                [bar]  AAA { $num ->
                           [one] One
                          *[other] Many { NUMBER($num) }
                       } BBB
        ''')

        self.assertEqual(
            ast.map(lambda x: x).toJSON(),
            ast.toJSON()
        )

    def test_copy_concat(self):
        node = FTL.Entity(
            FTL.Identifier('hello'),
            value=CONCAT(
                COPY(
                    SOURCE('path1', 'key1')
                ),
                COPY(
                    SOURCE('path2', 'key2')
                )
            )
        )

        result = node.map(lambda x: x)

        self.assertEqual(
            result.value.patterns[0].source.key,
            'key1'
        )
        self.assertEqual(
            result.value.patterns[1].source.key,
            'key2'
        )


class TestReduce(unittest.TestCase):
    def test_pattern(self):
        node = FTL.Entity(
            id=FTL.Identifier('key'),
            value=FTL.Pattern(
                source=None,
                elements=[
                    FTL.TextElement('Value')
                ]
            )
        )

        def get_value(acc, cur):
            if isinstance(cur, FTL.TextElement):
                return acc + (cur.value,)
            return acc

        self.assertEqual(
            fold_ftl(get_value, node, ()),
            ('Value',)
        )

    def test_copy_value(self):
        node = FTL.Entity(
            id=FTL.Identifier('key'),
            value=COPY(
                SOURCE('path', 'key')
            )
        )

        self.assertEqual(
            fold_ftl(get_source, node, ()),
            (('path', 'key'),)
        )

    def test_copy_traits(self):
        node = FTL.Entity(
            id=FTL.Identifier('key'),
            traits=[
                FTL.Member(
                    FTL.Keyword('trait1'),
                    value=COPY(
                        SOURCE('path1', 'key1')
                    )
                ),
                FTL.Member(
                    FTL.Keyword('trait2'),
                    value=COPY(
                        SOURCE('path2', 'key2')
                    )
                )
            ]
        )

        self.assertEqual(
            fold_ftl(get_source, node, ()),
            (('path1', 'key1'), ('path2', 'key2'))
        )

    def test_copy_concat(self):
        node = FTL.Entity(
            FTL.Identifier('hello'),
            value=CONCAT(
                COPY(
                    SOURCE('path1', 'key1')
                ),
                COPY(
                    SOURCE('path2', 'key2')
                )
            )
        )

        self.assertEqual(
            fold_ftl(get_source, node, ()),
            (('path1', 'key1'), ('path2', 'key2'))
        )
