#!/usr/bin/python3
"""Rectangle Class"""


class Rectangle:
    """Defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize the data width and the height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width"""
        return self.__width

    @property
    def height(self):
        """Get the height"""
        return self.__height

    @width.setter
    def width(self, value):
        """Set the widthfor the rectangle"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """Set the height for the rectangle"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Get the area"""
        return self.__width * self.__height
    
    def perimeter(self):
        """Get the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2
