#!/usr/bin/python3
"""Magic Class"""
import math


class MagicClass:
    """A Magic class that define the area and the circunference"""
    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Return the area"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Return the circum"""
        return 2 * math.pi * self.__radius
