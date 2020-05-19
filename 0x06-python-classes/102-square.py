#!/usr/bin/python3
"""Square Class"""


class Square:
    """A Square class that define the size"""
    def __init__(self, size=0):
        """ Initialize the size"""
        self.size = size

    @property
    def size(self):
        """Get the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size"""
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if (value < 0):
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Return the area of the square"""
        return self.__size**2

    def __lt__(self, other):
        """The less than comparison"""
        return self.area() < other.area()

    def __le__(self, other):
        """The less than or equal than comparison"""
        return self.area() <= other.area()

    def __eq__(self, other):
        """The equal to comparison"""
        return self.area() == other.area()

    def __ne__(self, other):
        """The not equal comparison"""
        return self.area() != other.area()

    def __gt__(self, other):
        """The greater than"""
        return self.area() > other.area()

    def __ge__(self, other):
        """The greater than or equal to"""
        return self.area() >= other.area()
