import os
import json
import pytest
from jsonschema import validate


def find_profiles():
    profiles = []
    for root, dirs, files in os.walk('assets'):
        path = root.split(os.sep)
        for _file in files:
            if _file.endswith('-data-package.json'):
                profiles.append(os.path.join(path[0], path[1], _file))
    return profiles


@pytest.mark.parametrize('profile_path', find_profiles())
def test_profile(profile_path):
    base_dir = os.path.dirname(profile_path)
    datapackage_path = os.path.join(base_dir, 'datapackage.json')

    with open(datapackage_path, 'r') as fp:
        datapackage_descriptor = json.load(fp)

    with open(profile_path, 'r') as fp:
        jsonschema = json.load(fp)

    validate(datapackage_descriptor, jsonschema)
