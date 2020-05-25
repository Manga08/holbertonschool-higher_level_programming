#!/usr/bin/python3
"""Rectangle Class"""


class Rectangle:
    """Defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize the data width and the height"""
        self.width = width
        self.height = height

    def __str__(self):
        """Print the rectangle with the '#'"""
        string = ''
        if self.__width == 0 or self.__height == 0:
            return string
        string += ('#' * self.__width + '\n') * self.__height
        return string[:-1]

    def __repr__(self):
        """String representation of the rectangle"""
        return ('Rectangle(' + str(self.__width) + ', ' +
                str(self.__height) + ')')

    def __del__(self):
        """Delete the rectangle"""
        print('Bye rectangle...')

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
        """Set the width for the rectangle"""
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
