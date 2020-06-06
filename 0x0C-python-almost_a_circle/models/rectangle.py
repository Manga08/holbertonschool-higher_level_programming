#!/usr/bin/python3
"""Rectangle Class."""
from models.base import Base


class Rectangle(Base):
    """Define a Rectangle class."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle parameters."""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """Print the Rectangle parameters."""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format
                (self.id, self.x, self.y, self.width, self.height))

    @property
    def width(self):
        """Get the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width."""
        self.int_validation('width', value)
        self.__width = value

    @property
    def height(self):
        """Get the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height."""
        self.int_validation('height', value)
        self.__height = value

    @property
    def x(self):
        """Get x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set x."""
        self.int_validation('x', value)
        self.__x = value

    @property
    def y(self):
        """Get y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y."""
        self.int_validation('y', value)
        self.__y = value

    def int_validation(self, name, value):
        """Validates all the value that recieves."""
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0 and (name == 'width' or name == 'height'):
            raise ValueError('{} must be > 0'.format(name))
        if value < 0 and (name == 'x' or name == 'y'):
            raise ValueError('{} must be >= 0'.format(name))

    def area(self):
        """Print the rectangle with the '#'."""
        return self.__width * self.__height

    def display(self):
        """Print the rectangle."""
        print('\n' * self.__y + (' ' * self.__x + '#' * self.__width + '\n') *
              self.__height, end='')
