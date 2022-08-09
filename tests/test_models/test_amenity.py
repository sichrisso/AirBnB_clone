#!/usr/bin/python3
"""
    This is a module test from Amenity class and your methods.
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    this class test Amenity class and your behavior
    """

    def setUp(self):
        self.amenity = Amenity()

    def test_creation(self):
        '''this test validate that creation proccess was correct.
        '''
        self.assertEqual(self.amenity.name, '')
