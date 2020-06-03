#!/usr/bin/python3
"""Student Class."""


class Student:
    """Represents a Student class."""
    def __init__(self, first_name, last_name, age):
        """Initialize the parameters."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns specific attributes of the student."""
        if attrs is None:
            return self.__dict__
        my_dict = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                my_dict[key] = value
        return my_dict
