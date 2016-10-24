# coding=utf8

import unittest

import l20n.format.ast as FTL

from util import ftl
from context import MergeContext
from operations import COPY, REPLACE


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

        MESSAGE = self.ctx.create_message()
        SOURCE = self.ctx.create_source()
        PLURALS = self.ctx.create_plurals()

        self.ctx.add_transforms([
            MESSAGE('aboutDownloads.ftl', 'title')(
                value=COPY(
                    SOURCE(
                        'aboutDownloads.dtd',
                        'aboutDownloads.title'
                    )
                )
            ),
            MESSAGE('aboutDownloads.ftl', 'header')(
                value=COPY(
                    SOURCE(
                        'aboutDownloads.dtd',
                        'aboutDownloads.header'
                    )
                )
            ),
            MESSAGE('aboutDownloads.ftl', 'empty')(
                value=COPY(
                    SOURCE(
                        'aboutDownloads.dtd',
                        'aboutDownloads.empty'
                    )
                )
            ),
            MESSAGE('aboutDownloads.ftl', 'open-menuitem')(
                traits=[
                    FTL.Member(
                        FTL.Keyword('label', 'html'),
                        COPY(
                            SOURCE(
                                'aboutDownloads.dtd',
                                'aboutDownloads.open'
                            )
                        )
                    )
                ]
            ),
            MESSAGE('aboutDownloads.ftl', 'retry-menuitem')(
                traits=[
                    FTL.Member(
                        FTL.Keyword('label', 'html'),
                        COPY(
                            SOURCE(
                                'aboutDownloads.dtd',
                                'aboutDownloads.retry'
                            )
                        )
                    )
                ]
            ),
            MESSAGE('aboutDownloads.ftl', 'remove-menuitem')(
                traits=[
                    FTL.Member(
                        FTL.Keyword('label', 'html'),
                        COPY(
                            SOURCE(
                                'aboutDownloads.dtd',
                                'aboutDownloads.remove'
                            )
                        )
                    )
                ]
            ),
            MESSAGE('aboutDownloads.ftl', 'pause-menuitem')(
                traits=[
                    FTL.Member(
                        FTL.Keyword('label', 'html'),
                        COPY(
                            SOURCE(
                                'aboutDownloads.dtd',
                                'aboutDownloads.pause'
                            )
                        )
                    )
                ]
            ),
            MESSAGE('aboutDownloads.ftl', 'resume-menuitem')(
                traits=[
                    FTL.Member(
                        FTL.Keyword('label', 'html'),
                        COPY(
                            SOURCE(
                                'aboutDownloads.dtd',
                                'aboutDownloads.resume'
                            )
                        )
                    )
                ]
            ),
            MESSAGE('aboutDownloads.ftl', 'cancel-menuitem')(
                traits=[
                    FTL.Member(
                        FTL.Keyword('label', 'html'),
                        COPY(
                            SOURCE(
                                'aboutDownloads.dtd',
                                'aboutDownloads.cancel'
                            )
                        )
                    )
                ]
            ),
            MESSAGE('aboutDownloads.ftl', 'remove-all-menuitem')(
                traits=[
                    FTL.Member(
                        FTL.Keyword('label', 'html'),
                        COPY(
                            SOURCE(
                                'aboutDownloads.dtd',
                                'aboutDownloads.removeAll'
                            )
                        )
                    )
                ]
            ),
            MESSAGE('aboutDownloads.ftl', 'delete-all-title')(
                value=COPY(
                    SOURCE(
                        'aboutDownloads.properties',
                        'downloadAction.deleteAll'
                    )
                )
            ),
            MESSAGE('aboutDownloads.ftl', 'delete-all-message')(
                value=PLURALS(
                    SOURCE(
                        'aboutDownloads.properties',
                        'downloadMessage.deleteAll'
                    ),
                    FTL.ExternalArgument('num'),
                    lambda var: REPLACE(
                        var,
                        {'#1': [FTL.ExternalArgument('num')]}
                    )
                )
            ),
            MESSAGE('aboutDownloads.ftl', 'download-state-downloading')(
                value=COPY(
                    SOURCE(
                        'aboutDownloads.properties',
                        'downloadState.downloading'
                    )
                )
            ),
            MESSAGE('aboutDownloads.ftl', 'download-state-canceled')(
                value=COPY(
                    SOURCE(
                        'aboutDownloads.properties',
                        'downloadState.canceled'
                    )
                )
            ),
            MESSAGE('aboutDownloads.ftl', 'download-state-failed')(
                value=COPY(
                    SOURCE(
                        'aboutDownloads.properties',
                        'downloadState.failed'
                    )
                )
            ),
            MESSAGE('aboutDownloads.ftl', 'download-state-paused')(
                value=COPY(
                    SOURCE(
                        'aboutDownloads.properties',
                        'downloadState.paused'
                    )
                )
            ),
            MESSAGE('aboutDownloads.ftl', 'download-state-starting')(
                value=COPY(
                    SOURCE(
                        'aboutDownloads.properties',
                        'downloadState.starting'
                    )
                )
            ),
            MESSAGE('aboutDownloads.ftl', 'download-size-unknown')(
                value=COPY(
                    SOURCE(
                        'aboutDownloads.properties',
                        'downloadState.unknownSize'
                    )
                )
            ),
        ])

    def test_merge_context_all_messages(self):
        expected = {
            'aboutDownloads.ftl': ftl('''
        # This Source Code Form is subject to the terms of the Mozilla Public
        # License, v. 2.0. If a copy of the MPL was not distributed with this
        # file, You can obtain one at http://mozilla.org/MPL/2.0/.

        title = Pobrane pliki
        header = Twoje pobrane pliki
        empty = Brak pobranych plików
        open-menuitem =
          [html/label] Otwórz
        retry-menuitem =
          [html/label] Spróbuj ponownie
        remove-menuitem =
          [html/label] Usuń
        pause-menuitem =
          [html/label] Wstrzymaj
        resume-menuitem =
          [html/label] Wznów
        cancel-menuitem =
          [html/label] Anuluj
        remove-all-menuitem =
          [html/label] Usuń wszystko
        delete-all-title = Usuń wszystko
        delete-all-message = { $num ->
          [one] Usunąć pobrany plik?
          [few] Usunąć { $num } pobrane pliki?
         *[many] Usunąć { $num } pobranych plików?
        }
        download-state-downloading = Pobieranie…
        download-state-canceled = Anulowane
        download-state-failed = Nieudane
        download-state-paused = Wstrzymane
        download-state-starting = Rozpoczynanie…
        download-size-unknown = Nieznany rozmiar
            ''')
        }

        self.assertDictEqual(
            self.ctx.merge(),
            expected
        )

    def test_merge_context_some_messages(self):

        changeset = {
            ('aboutDownloads.dtd', 'aboutDownloads.title'),
            ('aboutDownloads.dtd', 'aboutDownloads.header'),
            ('aboutDownloads.properties', 'downloadState.downloading'),
            ('aboutDownloads.properties', 'downloadState.canceled'),
        }

        expected = {
            'aboutDownloads.ftl': ftl('''
        # This Source Code Form is subject to the terms of the Mozilla Public
        # License, v. 2.0. If a copy of the MPL was not distributed with this
        # file, You can obtain one at http://mozilla.org/MPL/2.0/.

        title = Pobrane pliki
        header = Twoje pobrane pliki
        download-state-downloading = Pobieranie…
        download-state-canceled = Anulowane
            ''')
        }

        self.assertDictEqual(
            self.ctx.merge(changeset),
            expected
        )
