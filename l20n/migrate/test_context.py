# coding=utf8

import unittest

import l20n.format.ast as FTL

from util import ftl, ftl_resource_to_json, to_json
from context import MergeContext
from transforms import SOURCE, COPY


class TestMergeContext(unittest.TestCase):
    def setUp(self):
        self.ctx = MergeContext(
            lang='pl',
            reference_dir='fixtures/en-US',
            localization_dir='fixtures/pl'
        )

        self.ctx.add_reference('aboutDownloads.ftl')
        self.ctx.add_localization('aboutDownloads.dtd')
        self.ctx.add_localization('aboutDownloads.properties')

    def test_merge_single_message(self):
        self.ctx.add_transforms('aboutDownloads.ftl', [
            FTL.Entity(
                id=FTL.Identifier('title'),
                value=COPY(
                    SOURCE(
                        'aboutDownloads.dtd',
                        'aboutDownloads.title'
                    )
                )
            ),
        ])

        expected = {
            'aboutDownloads.ftl': ftl_resource_to_json('''
        # This Source Code Form is subject to the terms of the Mozilla Public
        # License, v. 2.0. If a copy of the MPL was not distributed with this
        # file, You can obtain one at http://mozilla.org/MPL/2.0/.

        title = Pobrane pliki
            ''')
        }

        self.assertDictEqual(
            to_json(self.ctx.merge_changeset()),
            expected
        )

    def test_merge_one_changeset(self):
        self.ctx.add_transforms('aboutDownloads.ftl', [
            FTL.Entity(
                id=FTL.Identifier('title'),
                value=COPY(
                    SOURCE(
                        'aboutDownloads.dtd',
                        'aboutDownloads.title'
                    )
                )
            ),
            FTL.Entity(
                id=FTL.Identifier('header'),
                value=COPY(
                    SOURCE(
                        'aboutDownloads.dtd',
                        'aboutDownloads.header'
                    )
                )
            ),
        ])

        changeset = {
            ('aboutDownloads.dtd', 'aboutDownloads.title'),
            ('aboutDownloads.dtd', 'aboutDownloads.header')
        }

        expected = {
            'aboutDownloads.ftl': ftl_resource_to_json('''
        # This Source Code Form is subject to the terms of the Mozilla Public
        # License, v. 2.0. If a copy of the MPL was not distributed with this
        # file, You can obtain one at http://mozilla.org/MPL/2.0/.

        title = Pobrane pliki
        header = Twoje pobrane pliki
            ''')
        }

        self.assertDictEqual(
            to_json(self.ctx.merge_changeset(changeset)),
            expected
        )

    def test_merge_two_changesets(self):
        self.ctx.add_transforms('aboutDownloads.ftl', [
            FTL.Entity(
                id=FTL.Identifier('title'),
                value=COPY(
                    SOURCE(
                        'aboutDownloads.dtd',
                        'aboutDownloads.title'
                    )
                )
            ),
            FTL.Entity(
                id=FTL.Identifier('header'),
                value=COPY(
                    SOURCE(
                        'aboutDownloads.dtd',
                        'aboutDownloads.header'
                    )
                )
            ),
        ])

        changeset_a = {
            ('aboutDownloads.dtd', 'aboutDownloads.title'),
        }

        changeset_b = {
            ('aboutDownloads.dtd', 'aboutDownloads.header')
        }

        expected_a = {
            'aboutDownloads.ftl': ftl_resource_to_json('''
        # This Source Code Form is subject to the terms of the Mozilla Public
        # License, v. 2.0. If a copy of the MPL was not distributed with this
        # file, You can obtain one at http://mozilla.org/MPL/2.0/.

        title = Pobrane pliki
            ''')
        }

        expected_b = {
            'aboutDownloads.ftl': ftl_resource_to_json('''
        # This Source Code Form is subject to the terms of the Mozilla Public
        # License, v. 2.0. If a copy of the MPL was not distributed with this
        # file, You can obtain one at http://mozilla.org/MPL/2.0/.

        title = Pobrane pliki
        header = Twoje pobrane pliki
            ''')
        }

        merged_a = to_json(self.ctx.merge_changeset(changeset_a))
        self.assertDictEqual(merged_a, expected_a)

        merged_b = to_json(self.ctx.merge_changeset(changeset_b))
        self.assertDictEqual(merged_b, expected_b)

    def test_serialize_changeset(self):
        self.ctx.add_transforms('aboutDownloads.ftl', [
            FTL.Entity(
                id=FTL.Identifier('title'),
                value=COPY(
                    SOURCE(
                        'aboutDownloads.dtd',
                        'aboutDownloads.title'
                    )
                )
            ),
            FTL.Entity(
                id=FTL.Identifier('header'),
                value=COPY(
                    SOURCE(
                        'aboutDownloads.dtd',
                        'aboutDownloads.header'
                    )
                )
            ),
        ])

        changesets = [
            {
                ('aboutDownloads.dtd', 'aboutDownloads.title'),
            },
            {
                ('aboutDownloads.dtd', 'aboutDownloads.header')
            }
        ]

        expected = iter([
            {
                'aboutDownloads.ftl': ftl('''
        # This Source Code Form is subject to the terms of the Mozilla Public
        # License, v. 2.0. If a copy of the MPL was not distributed with this
        # file, You can obtain one at http://mozilla.org/MPL/2.0/.

        title = Pobrane pliki
                ''')
            },
            {
                'aboutDownloads.ftl': ftl('''
        # This Source Code Form is subject to the terms of the Mozilla Public
        # License, v. 2.0. If a copy of the MPL was not distributed with this
        # file, You can obtain one at http://mozilla.org/MPL/2.0/.

        title = Pobrane pliki
        header = Twoje pobrane pliki
                ''')
            }
        ])

        for changeset in changesets:
            serialized = self.ctx.serialize_changeset(changeset)
            self.assertEqual(serialized, next(expected))
