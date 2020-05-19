#!/usr/bin/python3
import math
"""Magic Class"""


class MagicClass:
    """The Magic class"""
    def __init__(self, radius=0):
        """A Square class that define radious"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """The Area"""
        return ((self.__radius) ** 2) * math.pi

    def circumference(self):
        """The Circum"""
        return 2 * math.pi * self.__radius
