# coding=utf8

import l20n.format.ast as FTL
from l20n.migrate import CONCAT, COPY, INTERPOLATE, REPLACE


def migrate(ctx):
    """Migrate about:dialog, part {index}"""

    ctx.add_reference('browser/aboutDialog.ftl', realpath='aboutDialog.ftl')
    ctx.add_legacy('browser/chrome/browser/aboutDialog.dtd')

    MESSAGE = ctx.create_message()
    SOURCE = ctx.create_source()

    ctx.add_transforms([
        MESSAGE('browser/aboutDialog.ftl', 'update-failed')(
            value=CONCAT(
                COPY(
                    SOURCE('browser/chrome/browser/aboutDialog.dtd', 'update.failed.start'),
                ),
                COPY('<a>'),
                COPY(
                    SOURCE('browser/chrome/browser/aboutDialog.dtd', 'update.failed.linkText'),
                ),
                COPY('</a>'),
                COPY(
                    SOURCE('browser/chrome/browser/aboutDialog.dtd', 'update.failed.end'),
                ),
            )
        ),
        MESSAGE('browser/aboutDialog.ftl', 'channel-desc')(
            value=CONCAT(
                COPY(
                    SOURCE('browser/chrome/browser/aboutDialog.dtd', 'channel.description.start'),
                ),
                INTERPOLATE('channelname'),
                COPY(
                    SOURCE('browser/chrome/browser/aboutDialog.dtd', 'channel.description.end'),
                )
            )
        ),
        MESSAGE('browser/aboutDialog.ftl', 'community')(
            value=CONCAT(
                REPLACE(
                    SOURCE('browser/chrome/browser/aboutDialog.dtd', 'community.start2'),
                    {
                        '&brandShortName;': [
                            FTL.ExternalArgument('brand-short-name')
                        ]
                    }
                ),
                COPY('<a>'),
                REPLACE(
                    SOURCE('browser/chrome/browser/aboutDialog.dtd', 'community.mozillaLink'),
                    {
                        '&vendorShortName;': [
                            FTL.ExternalArgument('vendor-short-name')
                        ]
                    }
                ),
                COPY('</a>'),
                COPY(
                    SOURCE('browser/chrome/browser/aboutDialog.dtd', 'community.middle2')
                ),
                COPY('<a>'),
                COPY(
                    SOURCE('browser/chrome/browser/aboutDialog.dtd', 'community.creditsLink')
                ),
                COPY('</a>'),
                COPY(
                    SOURCE('browser/chrome/browser/aboutDialog.dtd', 'community.end3')
                )
            )
        ),
    ])
