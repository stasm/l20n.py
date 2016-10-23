# coding=utf8

import l20n.format.ast as FTL


def get_transform(transforms, ident):
    for transform in transforms:
        if transform.id.name == ident:
            return transform
    return None


def merge(reference, legacy, transforms):
    body = []

    for entry in reference['body']:
        transform = get_transform(transforms, entry['id']['name'])
        if transform:
            body.append(transform)

    return FTL.Resource(body, reference['comment'])
