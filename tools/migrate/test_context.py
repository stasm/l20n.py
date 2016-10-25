# coding=utf8

import unittest

from util import ftl, map_serialize
from context import MergeContext
from operations import COPY


class TestMergeContext(unittest.TestCase):
    def setUp(self):
        self.ctx = MergeContext(
            lang='pl',
            reference_dir='fixtures/en-US',
            localization_dir='fixtures/pl'
        )

        self.ctx.add_reference('aboutDownloads.ftl')
        self.ctx.add_legacy('aboutDownloads.dtd')
        self.ctx.add_legacy('aboutDownloads.properties')

    def test_merge_context_single_message(self):
        MESSAGE = self.ctx.create_message()
        SOURCE = self.ctx.create_source()

        self.ctx.add_transforms([
            MESSAGE('aboutDownloads.ftl', 'title')(
                value=COPY(
                    SOURCE(
                        'aboutDownloads.dtd',
                        'aboutDownloads.title'
                    )
                )
            ),
        ])

        expected = {
            'aboutDownloads.ftl': ftl('''
        # This Source Code Form is subject to the terms of the Mozilla Public
        # License, v. 2.0. If a copy of the MPL was not distributed with this
        # file, You can obtain one at http://mozilla.org/MPL/2.0/.

        title = Pobrane pliki
            ''')
        }

        self.assertDictEqual(
            map_serialize(self.ctx.merge_changeset()),
            expected
        )
