#!/usr/bin/python3
"""Unittest for base.py Module"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import pep8


class TestBase(unittest.TestCase):

    def test_Basic_Things(self):
        self.b1 = Base(1)
        self.b2 = Base(2)
        self.b3 = Base(-3)
        self.b4 = Base("Test.,/|<>")
        self.b5 = Base("Hola")
        self.b6 = Base(3.1)
        self.b7 = Base(-23)

    def test_correct_type(self):
        b1 = Base()
        self.assertTrue(type(b1) == Base)

    def test_nb_objects(self):
        b0 = Base()
        self.assertTrue(hasattr(b0, '_Base__nb_objects'))
        Base._Base__nb_objects = 0

    def test_class(self):
        b0 = Base()
        self.assertTrue(isinstance(b0, Base))

    def test_Base_equal(self):
        b1 = Base(13)
        self.assertEqual(b1.id, 13)
        b2 = Base(-13)
        self.assertEqual(b2.id, -13)
        b3 = Base("hola")
        self.assertEqual(b3.id, "hola")
        b4 = Base(13.1)
        self.assertEqual(b4.id, 13.1)
        b5 = Base(3)
        self.assertEqual(b5.id, 3)
        Base._Base__nb_objects = 0

    def test_json_to_string_rec(self):
        Rec = Rectangle(13, 1, 2, 8, 9)
        dic = Rec.to_dictionary()
        json_Dict = Base.to_json_string([dic])
        self.assertEqual(type(json_Dict), str)

    def test_json_to_string_sq(self):
        Sq = Square(13, 1, 2, 8)
        dic = Sq.to_dictionary()
        json_Dict = Base.to_json_string([dic])
        self.assertEqual(type(json_Dict), str)

    def test_all_pep8_fl(self):
        msg = "Found code style errors (and warning)."
        style = pep8.StyleGuide(quiet=True)
        fl_Base = "models/base.py"
        fl_Base_tst = "tests/test_base.py"
        fl_Rec = "models/rectangle.py"
        fl_Rec_tst = "tests/test_rectangle.py"
        fl_Sq = "models/square.py"
        fl_Sq_tst = "tests/test_square.py"
        check = style.check_files([fl_Rec, fl_Rec_tst, fl_Base, fl_Base_tst,
                                   fl_Sq, fl_Sq_tst])
        self.assertEqual(check.total_errors, 0, msg)

    def test_save_to_file_rec(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json") as fl:
            self.assertEqual(fl.read(), '[]')

    def test_save_to_file_sq(self):
        Square.save_to_file([])
        with open("Square.json") as fl:
            self.assertEqual(fl.read(), '[]')
