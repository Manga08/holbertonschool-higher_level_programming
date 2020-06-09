#!/usr/bin/python3
"""Test Rectangle Module"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class Test_Rectangle(unittest.TestCase):
    """Test Rectangle with unittest."""

    def test_Parameters(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)

        self.assertEqual(r3.id, 12)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)

    def test_area(self):
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r1.area(), 6)
        self.assertEqual(r2.area(), 20)
        self.assertEqual(r3.area(), 56)

    def test_display(self):
        r1 = Rectangle(1, 1)
        self.assertTrue(hasattr(r1, 'display'))
        Base._Base__nb_objects = 0

    def test_str(self):
        Base._Base__nb_objects = 0
        r1 = Rectangle(13, 13)
        string_rep = r1.__str__()
        self.assertEqual(string_rep, "[Rectangle] (1) 0/0 - 13/13")

    def test_to_dictionary(self):
        Base._Base__nb_objects = 0
        r1 = Rectangle(13, 3, 0, 1)
        r1_dict = r1.to_dictionary()
        self.assertEqual({"id": 1, "width": 13, "height": 3, "x": 0, "y": 1},
                         r1_dict)
