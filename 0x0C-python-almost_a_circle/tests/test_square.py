#!/usr/bin/python3
"""Test Rectangle Module"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Rectangle(unittest.TestCase):
    """Test Rectangle with unittest."""

    def test_size_parameter(self):
        s1 = Square(3)
        s2 = Square(2, 2)
        s3 = Square(3, 2, 4, 13)
        self.assertEqual(s1.size, 3)
        self.assertEqual(s2.size, 2)
        self.assertEqual(s3.size, 3)

    def test_str(self):
        Base._Base__nb_objects = 0
        s1 = Square(13, 13)
        string_rep = s1.__str__()
        self.assertEqual(string_rep, "[Square] (1) 13/0 - 13")

    def test_to_dictionary(self):
        Base._Base__nb_objects = 0
        s1 = Square(13, 3, 0, 1)
        s1_dict = s1.to_dictionary()
        self.assertEqual({'id': 1, 'size': 13, 'x': 3, 'y': 0}, s1_dict)

    def test_Update(self):
        s1 = Square(size=5, x=15, y=20, id=100)
        s2 = Square(2, 5, 1, 10)
        s2.update(x=1, size=2, y=3)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 15)
        self.assertEqual(s1.y, 20)
        self.assertEqual(s1.id, 100)
        self.assertEqual(s2.x, 1)
        self.assertEqual(s2.size, 2)
        self.assertEqual(s2.y, 3)
