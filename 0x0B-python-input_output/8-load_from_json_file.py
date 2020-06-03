#!/usr/bin/python3
"""load_from_json_file Module."""


def load_from_json_file(filename):
    """Creates an Object from a 'JSON file'."""
    import json
    with open(filename, 'r') as fl:
        return json.loads(fl.read())
