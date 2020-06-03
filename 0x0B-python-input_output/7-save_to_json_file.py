#!/usr/bin/python3
"""save_to_json_file Module."""


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON."""
    import json
    with open(filename, 'w') as fl:
        fl.write(json.dumps(my_obj))
