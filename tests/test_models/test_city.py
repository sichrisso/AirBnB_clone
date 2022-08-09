#!/usr/bin/env python3
"""
    This is a module test from City class and your methods.
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """
    this class test City class and your behavior
    """

    def setUp(self):
        self.city = City()

    def test_creation(self):
        '''this test validate that creation proccess was correct.
        '''
        self.assertEqual(self.city.name, '')
