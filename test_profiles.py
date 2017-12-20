import os
import json
from jsonschema import validate

PROFILES = [
    'assets/trees/trees-data-package.json',
    'assets/grants/grants-data-package.json',
]


def find_profiles():
    profiles = []
    for root, dirs, files in os.walk('assets'):
        path = root.split(os.sep)
        for _file in files:
            if _file.endswith('-data-package.json'):
                profiles.append(os.path.join(path[0], path[1], _file))
    return profiles

for profile in find_profiles():
    base_dir = os.path.dirname(profile)

    data_package_descriptor = json.load(
        open(os.path.join(base_dir, 'datapackage.json'), 'r'))

    json_schema = json.load(open(profile, 'r'))

    validate(data_package_descriptor, json_schema)

    print('Validation for profile {} OK'.format(profile))
