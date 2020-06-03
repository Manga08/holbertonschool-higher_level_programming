#!/usr/bin/python3
"""Module of Rectangle Class."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class Rectangle that inherits from BaseGeometry."""
    def __init__(self, width, height):
        """Rectangle parameters."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
