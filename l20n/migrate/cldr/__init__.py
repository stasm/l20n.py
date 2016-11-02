# coding=utf8

import codecs
import json
import os


def path(*args):
    return os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        *args
    )

cldr_plurals = json.load(codecs.open(path('plurals.json'), 'r', 'utf8'))
rules = cldr_plurals['supplemental']['plurals-type-cardinal']

canonical_order = ('zero', 'one', 'two', 'few', 'many', 'other')


def in_canonical_order(a, b):
    return canonical_order.index(a) - canonical_order.index(b)


categories = {}

for lang, rules in rules.items():
    categories[lang] = sorted(map(
        lambda key: key.replace('pluralRule-count-', ''),
        rules.keys()
    ), in_canonical_order)


def get_plural_categories(lang):
    return categories.get(lang, None)
