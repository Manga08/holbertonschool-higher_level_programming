#!/usr/bin/python3
"""Base class"""
import json
from os import path


class Base:
    """Define a Base class."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base parameters."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON representation of an object."""
        if not list_dictionaries or list_dictionaries is None:
            return '[]'
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns an object represented by a JSON string"""
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes an Object to a text file, using a JSON."""
        dic = []
        if list_objs:
            for ct in list_objs:
                dic.append(cls.to_dictionary(ct))
        with open(cls.__name__ + ".json", "w") as fl:
            fl.write(cls.to_json_string(dic))

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        "Returns a list of instances."
        if not path.isfile(cls.__name__ + ".json"):
            return []
        with open(cls.__name__ + ".json", "r") as fl:
            return [cls.create(**ct) for ct in cls.from_json_string(fl.read())]
