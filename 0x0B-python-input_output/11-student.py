#!/usr/bin/python3
"""Student Class."""


class Student:
    """Represents a Student class."""
    def __init__(self, first_name, last_name, age):
        """Initialize the parameters."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dictionary."""
        return self.__dict__
