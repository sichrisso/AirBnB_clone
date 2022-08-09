#!/usr/bin/python3
"""
    This is a module test from Place class and your methods.
"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    this class test Place class and your behavior
    """

    def setUp(self):
        self.place = Place()

    def test_creation(self):
        '''this test validate that creation proccess was correct.
        '''
        self.assertEqual(self.place.name, '')
