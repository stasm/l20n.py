# coding=utf8

import l20n.format.ast as FTL
from l20n.migrate import CONCAT, COPY, INTERPOLATE, REPLACE


def migrate(ctx):
    ctx.add_reference('aboutDialog.ftl')
    ctx.add_legacy('aboutDialog.dtd')

    MESSAGE = ctx.create_message()
    SOURCE = ctx.create_source()

    ctx.add_transforms([
        MESSAGE('aboutDialog.ftl', 'update-failed')(
            value=CONCAT(
                COPY(
                    SOURCE('aboutDialog.dtd', 'update.failed.start'),
                ),
                COPY('<a>'),
                COPY(
                    SOURCE('aboutDialog.dtd', 'update.failed.linkText'),
                ),
                COPY('</a>'),
                COPY(
                    SOURCE('aboutDialog.dtd', 'update.failed.end'),
                ),
            )
        ),
        MESSAGE('aboutDialog.ftl', 'channel-desc')(
            value=CONCAT(
                COPY(
                    SOURCE('aboutDialog.dtd', 'channel.description.start'),
                ),
                INTERPOLATE('channelname'),
                COPY(
                    SOURCE('aboutDialog.dtd', 'channel.description.end'),
                )
            )
        ),
        MESSAGE('aboutDialog.ftl', 'community')(
            value=CONCAT(
                REPLACE(
                    SOURCE('aboutDialog.dtd', 'community.start'),
                    {
                        '&brandShortName;': [
                            FTL.ExternalArgument('brand-short-name')
                        ]
                    }
                ),
                COPY('<a>'),
                REPLACE(
                    SOURCE('aboutDialog.dtd', 'community.mozillaLink'),
                    {
                        '&vendorShortName;': [
                            FTL.ExternalArgument('vendor-short-name')
                        ]
                    }
                ),
                COPY('</a>'),
                COPY(
                    SOURCE('aboutDialog.dtd', 'community.middle')
                ),
                COPY('<a>'),
                COPY(
                    SOURCE('aboutDialog.dtd', 'community.creditsLink')
                ),
                COPY('</a>'),
                COPY(
                    SOURCE('aboutDialog.dtd', 'community.end')
                )
            )
        ),
    ])
