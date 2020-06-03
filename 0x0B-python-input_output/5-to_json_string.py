#!/usr/bin/python3
"""function that represents JSON."""


def to_json_string(my_obj):
    """Returns the JSON representation of an object."""
    import json
    return json.dumps(my_obj)
