#!/usr/bin/python3
"""Square Class"""


class Square:
    """A Square class that define the size"""
    def __init__(self, size=0):
        """Initialize the size"""
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
        return (self.__size * self.__size)

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if (self.size != 0):
            for ct in range(self.__size):
                for ct2 in range(self.__size):
                    print("#", end='')
                print('')
        else:
            print('')
