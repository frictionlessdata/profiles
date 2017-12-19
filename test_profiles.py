import os
import json
from jsonschema import validate

PROFILES = [
    'assets/trees/trees-data-package.json',
    'assets/grants/grants-data-package.json',
]


for profile in PROFILES:
    base_dir = os.path.dirname(profile)

    data_package_descriptor = json.load(
        open(os.path.join(base_dir, 'datapackage.json'), 'r'))

    json_schema = json.load(open(profile, 'r'))

    validate(data_package_descriptor, json_schema)
