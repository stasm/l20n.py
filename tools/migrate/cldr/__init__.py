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

categories = {}

for lang, rules in rules.items():
    categories[lang] = map(
        lambda key: key.replace('pluralRule-count-', ''),
        rules.keys()
    )


def get_plural_categories(lang):
    return categories.get(lang, None)
