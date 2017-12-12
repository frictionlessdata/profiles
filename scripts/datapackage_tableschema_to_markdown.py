#!/usr/bin/env python3
import json
import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Convert Data Package Table Schema to a Markdown table'
    )
    parser.add_argument(
        '--index',
        type=int,
        default=0,
        help='index of the resource to convert'
    )
    parser.add_argument(
        'path',
        help='path to datapackage.json'
    )
    args = parser.parse_args()

    print(datapackage_to_markdown(args.path, args.index))


def datapackage_to_markdown(path, resource_index=0):
    with open(path, 'r') as fp:
        dp = json.load(fp)

    assert dp.get('resources'), 'Data Package must have at least one resource'
    assert len(dp['resources']) >= (resource_index + 1), \
        'Resource index "{}" doesn\'t exist'.format(resource_index)

    resource = dp['resources'][resource_index]
    assert resource.get('schema'), 'The resource must have an schema'

    return schema_to_markdown(resource['schema'])

def schema_to_markdown(schema):
    headers = [
        'name',
        'title',
        'type',
        'constraints',
    ]

    rows = [
        [header.capitalize() for header in headers],
        ['---'] * len(headers),
    ]
    for field in schema.get('fields', []):
        row = [
            _attribute_to_str(field.get(header))
            for header in headers
        ]
        rows.append(row)

    return '\n'.join([
        '| {} |'.format(' | '.join(row))
        for row in rows
    ])


def _attribute_to_str(attr):
    if attr is None:
        result = ''
    elif isinstance(attr, dict):
        result = '\n'.join([
            '**{key}**: {value}'.format(
                key=key, value=str(value)
            )
            for key, value in attr.items()
        ])
    else:
        result = str(attr)

    return result


if __name__ == '__main__':
    main()
