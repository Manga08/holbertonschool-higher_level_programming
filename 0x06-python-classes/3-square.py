#!/usr/bin/python3
"""Square Class"""


class Square:
    """A Square class that define the size"""

    def __init__(self, size=0):
        """Initializes the variables"""

        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

        def area(self):
            """Return the area of the square"""
            return self.__size**2
