# coding=utf8

import unittest

import l20n.format.ast as FTL
from l20n.format.parser import FTLParser
from compare_locales.parser import PropertiesParser, DTDParser
from util import parse, serialize, ftl

from merge import merge
from operations import COPY


# Mock SOURCE using the collection parsed in setUp.
def SOURCE(collection, key):
    return collection.get(key, None).get_val()


class TestMerge(unittest.TestCase):
    def setUp(self):
        self.en_us_ftl = parse(FTLParser, ftl('''
            # This Source Code Form is subject to the terms of …

            title  = Downloads
            header = Your Downloads
            empty  = No Downloads

            open-menuitem =
                [html/label] Open

            download-state-downloading = Downloading…
        '''))

        self.ab_cd_ftl = parse(FTLParser, ftl('''
            # This Source Code Form is subject to the terms of …

            empty = Brak pobranych plików
        '''))

        ab_cd_dtd = parse(DTDParser, '''
            <!ENTITY aboutDownloads.title "Pobrane pliki">
            <!ENTITY aboutDownloads.open "Otwórz">
        ''')

        ab_cd_prop = parse(PropertiesParser, '''
            downloadState.downloading=Pobieranie…
        ''')

        self.ab_cd_legacy = {
            key: val
            for strings in (ab_cd_dtd, ab_cd_prop)
            for key, val in strings.items()
        }

    def test_merge_two_way(self):
        transforms = [
            FTL.Entity(
                FTL.Identifier('title'),
                value=COPY(
                    SOURCE(self.ab_cd_legacy, 'aboutDownloads.title')
                )
            ),
            FTL.Entity(
                FTL.Identifier('open-menuitem'),
                traits=[
                    FTL.Member(
                        FTL.Keyword('label', 'html'),
                        COPY(
                            SOURCE(self.ab_cd_legacy, 'aboutDownloads.open')
                        )
                    ),
                ]
            ),
            FTL.Entity(
                FTL.Identifier('download-state-downloading'),
                value=COPY(
                    SOURCE(self.ab_cd_legacy, 'downloadState.downloading')
                )
            )
        ]

        resource = merge(
            self.en_us_ftl, FTL.Resource(), transforms
        )

        self.assertEqual(
            serialize(resource),
            ftl('''
                # This Source Code Form is subject to the terms of …

                title = Pobrane pliki
                open-menuitem =
                  [html/label] Otwórz
                download-state-downloading = Pobieranie…
            ''')
        )

    def test_merge_three_way(self):
        transforms = [
            FTL.Entity(
                FTL.Identifier('title'),
                value=COPY(
                    SOURCE(self.ab_cd_legacy, 'aboutDownloads.title')
                )
            ),
            FTL.Entity(
                FTL.Identifier('open-menuitem'),
                traits=[
                    FTL.Member(
                        FTL.Keyword('label', 'html'),
                        COPY(
                            SOURCE(self.ab_cd_legacy, 'aboutDownloads.open')
                        )
                    ),
                ]
            ),
            FTL.Entity(
                FTL.Identifier('download-state-downloading'),
                value=COPY(
                    SOURCE(self.ab_cd_legacy, 'downloadState.downloading')
                )
            )
        ]

        resource = merge(
            self.en_us_ftl, self.ab_cd_ftl, transforms
        )

        self.assertEqual(
            serialize(resource),
            ftl('''
                # This Source Code Form is subject to the terms of …

                title = Pobrane pliki
                empty = Brak pobranych plików
                open-menuitem =
                  [html/label] Otwórz
                download-state-downloading = Pobieranie…
            ''')
        )
