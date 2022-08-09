#!/usr/bin/env python3
"""
    This is a module test from BaseModel class and your methods.
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """
    this class test user class and your behavior
    """

    def setUp(self):
        self.state = State()

    def test_creation(self):
        '''this test validate that creation proccess was correct.
        '''
        self.assertEqual(self.State.name, '')
