#!/usr/bin/python3
"""Square Class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Define a Square Class."""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the Square parameters from the Rectangle."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Print the Square parameters."""
        return("[Square] ({}) {}/{} - {}".format
               (self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """Get the size."""
        return (self.width)

    @size.setter
    def size(self, value):
        """Set the size."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the attributes of the class."""
        attrs = ["id", "size", "x", "y"]

        for num_attr, num_arg in zip(attrs, args):
            setattr(self, num_attr, num_arg)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """Returns a dictionary of the Square parameters."""
        dic = {}
        dic["id"] = self.id
        dic["size"] = self.size
        dic["x"] = self.x
        dic["y"] = self.y
        return dic
