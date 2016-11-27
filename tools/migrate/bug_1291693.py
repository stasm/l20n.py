# coding=utf8

import l20n.format.ast as FTL
from l20n.migrate import LITERAL_FROM, REPLACE_FROM


def migrate(ctx):
    """Bug 1291693 - Migrate the menubar to FTL, part {index}"""

    ctx.add_reference(
        'browser/menubar.ftl',
        realpath='browser/locales/en-US/browser/menubar.ftl'
    )
    ctx.add_reference(
        'browser/toolbar.ftl',
        realpath='browser/locales/en-US/browser/toolbar.ftl'
    )
    ctx.add_reference(
        'browser/branding/official/brand.ftl',
        realpath='browser/branding/official/locales/en-US/brand.ftl'
    )

    ctx.add_localization('browser/chrome/browser/browser.dtd')
    ctx.add_localization('browser/chrome/browser/browser.properties')
    ctx.add_localization('browser/branding/official/brand.dtd')
    ctx.add_localization('browser/branding/official/brand.properties')

    ctx.add_transforms('browser/menubar.ftl', [
        FTL.Entity(
            id=FTL.Identifier('file-menu'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'fileMenu.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'fileMenu.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('tab-menuitem'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'tabCmd.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'tabCmd.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('tab-command'),
            traits=[
                FTL.Member(
                    FTL.Keyword('key', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'tabCmd.commandkey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('new-user-context-menu'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'newUserContext.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'newUserContext.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('new-navigator-menuitem'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'newNavigatorCmd.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'newNavigatorCmd.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('new-navigator-command'),
            traits=[
                FTL.Member(
                    FTL.Keyword('key', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'newNavigatorCmd.key',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('new-private-window-menuitem'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'newPrivateWindow.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'newPrivateWindow.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('new-non-remote-window-menuitem'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'newNonRemoteWindow.label',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('open-location-menuitem'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'openLocationCmd.label',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('open-file-menuitem'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'openFileCmd.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'openFileCmd.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('open-file-command'),
            traits=[
                FTL.Member(
                    FTL.Keyword('key', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'openFileCmd.commandkey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('close-menuitem'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'closeCmd.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'closeCmd.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('close-command'),
            traits=[
                FTL.Member(
                    FTL.Keyword('key', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'closeCmd.key',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('close-window-menuitem'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'closeWindow.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'closeWindow.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('save-page-menuitem'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'savePageCmd.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'savePageCmd.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('save-page-command'),
            traits=[
                FTL.Member(
                    FTL.Keyword('key', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'savePageCmd.commandkey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('email-page-menuitem'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'emailPageCmd.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'emailPageCmd.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('print-setup-menuitem'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'printSetupCmd.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'printSetupCmd.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('print-preview-menuitem'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'printPreviewCmd.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'printPreviewCmd.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('print-menuitem'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'printCmd.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'printCmd.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('print-command'),
            traits=[
                FTL.Member(
                    FTL.Keyword('key', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'printCmd.commandkey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('go-offline-menuitem'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'goOfflineCmd.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'goOfflineCmd.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('quit-application-menuitem'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'quitApplicationCmd.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'quitApplicationCmd.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('quit-application-menuitem-win'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'quitApplicationCmdWin2.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'quitApplicationCmdWin2.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('quit-application-menuitem-mac'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'quitApplicationCmdMac2.label',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('quit-application-command-unix'),
            traits=[
                FTL.Member(
                    FTL.Keyword('key', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'quitApplicationCmdUnix.key',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('edit-menu'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'editMenu.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'editMenu.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('undo-menuitem'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'undoCmd.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'undoCmd.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('undo-command'),
            traits=[
                FTL.Member(
                    FTL.Keyword('key', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'undoCmd.key',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('redo-menuitem'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'redoCmd.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'redoCmd.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('redo-command'),
            traits=[
                FTL.Member(
                    FTL.Keyword('key', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'redoCmd.key',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('cut-menuitem'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'cutCmd.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'cutCmd.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('cut-command'),
            traits=[
                FTL.Member(
                    FTL.Keyword('key', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'cutCmd.key',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('copy-menuitem'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'copyCmd.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'copyCmd.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('copy-command'),
            traits=[
                FTL.Member(
                    FTL.Keyword('key', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'copyCmd.key',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('paste-menuitem'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'pasteCmd.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'pasteCmd.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('paste-command'),
            traits=[
                FTL.Member(
                    FTL.Keyword('key', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'pasteCmd.key',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('delete-menuitem'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'deleteCmd.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'deleteCmd.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('select-all-menuitem'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'selectAllCmd.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'selectAllCmd.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('select-all-command'),
            traits=[
                FTL.Member(
                    FTL.Keyword('key', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'selectAllCmd.key',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('find-on-menuitem'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'findOnCmd.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'findOnCmd.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('find-on-command'),
            traits=[
                FTL.Member(
                    FTL.Keyword('key', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'findOnCmd.commandkey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('find-again-menuitem'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'findAgainCmd.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'findAgainCmd.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('find-again-command1'),
            traits=[
                FTL.Member(
                    FTL.Keyword('key', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'findAgainCmd.commandkey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('find-again-command2'),
            traits=[
                FTL.Member(
                    FTL.Keyword('key', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'findAgainCmd.commandkey2',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('find-selection-command'),
            traits=[
                FTL.Member(
                    FTL.Keyword('key', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'findSelectionCmd.commandkey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('bidi-switch-text-direction-menuitem'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'bidiSwitchTextDirectionItem.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'bidiSwitchTextDirectionItem.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('bidi-switch-text-direction-command'),
            traits=[
                FTL.Member(
                    FTL.Keyword('key', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'bidiSwitchTextDirectionItem.commandkey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('preferences-menuitem'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'preferencesCmd2.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'preferencesCmd2.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('preferences-menuitem-unix'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'preferencesCmdUnix.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'preferencesCmdUnix.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('view-menu'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'viewMenu.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'viewMenu.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('view-toolbar-menu'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'viewToolbarsMenu.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'viewToolbarsMenu.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('view-sidebar-menu'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'viewSidebarMenu.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'viewSidebarMenu.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('view-customize-toolbar-menuitem'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'viewCustomizeToolbar.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'viewCustomizeToolbar.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('full-zoom-menu'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'fullZoom.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'fullZoom.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('full-zoom-enlarge-menuitem'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'fullZoomEnlargeCmd.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'fullZoomEnlargeCmd.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('full-zoom-enlarge-command1'),
            traits=[
                FTL.Member(
                    FTL.Keyword('key', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'fullZoomEnlargeCmd.commandkey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('full-zoom-enlarge-command2'),
            traits=[
                FTL.Member(
                    FTL.Keyword('key', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'fullZoomEnlargeCmd.commandkey2',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('full-zoom-enlarge-command3'),
            traits=[
                FTL.Member(
                    FTL.Keyword('key', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'fullZoomEnlargeCmd.commandkey3',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('full-zoom-reduce-menuitem'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'fullZoomReduceCmd.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'fullZoomReduceCmd.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('full-zoom-reduce-command1'),
            traits=[
                FTL.Member(
                    FTL.Keyword('key', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'fullZoomReduceCmd.commandkey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('full-zoom-reduce-command2'),
            traits=[
                FTL.Member(
                    FTL.Keyword('key', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'fullZoomReduceCmd.commandkey2',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('full-zoom-reset-menuitem'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'fullZoomResetCmd.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'fullZoomResetCmd.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('full-zoom-reset-command1'),
            traits=[
                FTL.Member(
                    FTL.Keyword('key', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'fullZoomResetCmd.commandkey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('full-zoom-reset-command2'),
            traits=[
                FTL.Member(
                    FTL.Keyword('key', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'fullZoomResetCmd.commandkey2',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('full-zoom-toggle-menuitem'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'fullZoomToggleCmd.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'fullZoomToggleCmd.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('page-style-menu'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'pageStyleMenu.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'pageStyleMenu.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('page-style-no-style-menuitem'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'pageStyleNoStyle.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'pageStyleNoStyle.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('page-style-persistent-only-menuitem'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'pageStylePersistentOnly.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'pageStylePersistentOnly.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('show-all-tabs-menuitem'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'showAllTabsCmd.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'showAllTabsCmd.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('bidi-switch-page-direction-menuitem'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'bidiSwitchPageDirectionItem.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'bidiSwitchPageDirectionItem.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('enter-full-screen-menuitem'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'enterFullScreenCmd.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'enterFullScreenCmd.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('exit-full-screen-menuitem'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'exitFullScreenCmd.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'exitFullScreenCmd.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('full-screen-menuitem'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'fullScreenCmd.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'fullScreenCmd.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('full-screen-command'),
            traits=[
                FTL.Member(
                    FTL.Keyword('key', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'fullScreenCmd.macCommandKey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('history-menu'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'historyMenu.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'historyMenu.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('show-all-history-menuitem'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'showAllHistoryCmd2.label',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('show-all-history-command'),
            traits=[
                FTL.Member(
                    FTL.Keyword('key', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'showAllHistoryCmd.commandkey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('clear-recent-history-menuitem'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'clearRecentHistory.label',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('history-synced-tabs-menuitem'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'syncTabsMenu3.label',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('history-restore-last-session-menuitem'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'historyRestoreLastSession.label',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('history-undo-menu'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'historyUndoMenu.label',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('history-undo-window-menu'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'historyUndoWindowMenu.label',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('bookmarks-menu'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'bookmarksMenu.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'bookmarksMenu.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('show-all-bookmarks-menuitem'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'showAllBookmarks2.label',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('show-all-bookmarks-command'),
            traits=[
                FTL.Member(
                    FTL.Keyword('key', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'bookmarksCmd.commandkey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('show-all-bookmarks-command-gtk'),
            traits=[
                FTL.Member(
                    FTL.Keyword('key', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'bookmarksGtkCmd.commandkey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('bookmark-this-page-broadcaster'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'bookmarkThisPageCmd.label',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('edit-this-page-broadcaster'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'editThisBookmarkCmd.label',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('bookmark-this-page-command'),
            traits=[
                FTL.Member(
                    FTL.Keyword('key', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'bookmarkThisPageCmd.commandkey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('subscribe-to-page-menuitem'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'subscribeToPageMenupopup.label',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('subscribe-to-page-menupopup'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'subscribeToPageMenupopup.label',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('add-cur-pages-menuitem'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'addCurPagesCmd.label',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('recent-bookmarks-menuitem'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'recentBookmarks.label',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('other-bookmarks-menu'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'otherBookmarksCmd.label',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('personalbar-menu'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'personalbarCmd.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'personalbarCmd.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('tools-menu'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'toolsMenu.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'toolsMenu.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('downloads-menuitem'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'downloads.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'downloads.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('downloads-command'),
            traits=[
                FTL.Member(
                    FTL.Keyword('key', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'downloads.commandkey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('downloads-command-unix'),
            traits=[
                FTL.Member(
                    FTL.Keyword('key', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'downloadsUnix.commandkey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('addons-menuitem'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'addons.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'addons.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('addons-command'),
            traits=[
                FTL.Member(
                    FTL.Keyword('key', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'addons.commandkey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('sync-sign-in-menuitem'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    REPLACE_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'syncSignIn.label',
                        {
                            '&syncBrand.shortName.label;': [
                                FTL.ExternalArgument('sync-brand-short-name')
                            ]
                        }
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'syncSignIn.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('sync-sync-now-menuitem'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'syncSyncNowItem.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'syncSyncNowItem.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('sync-re-auth-menuitem'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    REPLACE_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'syncReAuthItem.label',
                        {
                            '&syncBrand.shortName.label;': [
                                FTL.ExternalArgument('sync-brand-short-name')
                            ]
                        }
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'syncReAuthItem.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('sync-toolbar-button'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'syncToolbarButton.label',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('web-developer-menu'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'webDeveloperMenu.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'webDeveloperMenu.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('page-source-broadcaster'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'pageSourceCmd.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'pageSourceCmd.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('page-source-command'),
            traits=[
                FTL.Member(
                    FTL.Keyword('key', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'pageSourceCmd.commandkey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('page-info-menuitem'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'pageInfoCmd.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'pageInfoCmd.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('page-info-command'),
            traits=[
                FTL.Member(
                    FTL.Keyword('key', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'pageInfoCmd.commandkey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('mirror-tab-menu'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'mirrorTabCmd.label',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'mirrorTabCmd.accesskey',
                    )
                ),
            ]
        ),
    ])

    ctx.add_transforms('browser/toolbar.ftl', [
        FTL.Entity(
            id=FTL.Identifier('urlbar-textbox'),
            traits=[
                FTL.Member(
                    FTL.Keyword('placeholder', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'urlbar.placeholder2',
                    )
                ),
                FTL.Member(
                    FTL.Keyword('accesskey', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'urlbar.accesskey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('view-bookmarks-broadcaster'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'bookmarksButton.label',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('view-bookmarks-command'),
            traits=[
                FTL.Member(
                    FTL.Keyword('key', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'bookmarksCmd.commandkey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('view-bookmarks-command-win'),
            traits=[
                FTL.Member(
                    FTL.Keyword('key', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'bookmarksWinCmd.commandkey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('view-history-broadcaster'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'historyButton.label',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('view-history-command'),
            traits=[
                FTL.Member(
                    FTL.Keyword('key', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'historySidebarCmd.commandkey',
                    )
                ),
            ]
        ),
        FTL.Entity(
            id=FTL.Identifier('view-tabs-broadcaster'),
            traits=[
                FTL.Member(
                    FTL.Keyword('label', 'xul'),
                    LITERAL_FROM(
                        'browser/chrome/browser/browser.dtd',
                        'syncedTabs.sidebar.label',
                    )
                ),
            ]
        ),
    ])

    ctx.add_transforms('browser/branding/official/brand.ftl', [
        FTL.Entity(
            id=FTL.Identifier('brand-shorter-name'),
            value=LITERAL_FROM(
                'browser/branding/official/brand.dtd',
                'brandShorterName'
            )
        ),
        FTL.Entity(
            id=FTL.Identifier('brand-short-name'),
            value=LITERAL_FROM(
                'browser/branding/official/brand.dtd',
                'brandShortName'
            )
        ),
        FTL.Entity(
            id=FTL.Identifier('brand-full-name'),
            value=LITERAL_FROM(
                'browser/branding/official/brand.dtd',
                'brandFullName'
            )
        ),
        FTL.Entity(
            id=FTL.Identifier('vendor-short-name'),
            value=LITERAL_FROM(
                'browser/branding/official/brand.dtd',
                'vendorShortName'
            )
        ),
        FTL.Entity(
            id=FTL.Identifier('trademark-info'),
            value=LITERAL_FROM(
                'browser/branding/official/brand.dtd',
                'trademarkInfo.part1'
            )
        ),
        FTL.Entity(
            id=FTL.Identifier('sync-brand-short-name'),
            value=LITERAL_FROM(
                'browser/branding/official/brand.properties',
                'syncBrandShortName'
            )
        ),
    ])
