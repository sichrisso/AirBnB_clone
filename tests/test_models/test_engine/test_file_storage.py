#!/usr/bin/python3
"""
    This is a module test from BaseModel class and your methods.
"""
from models.engine.file_storage import FileStorage
import unittest
from models.engine.file_storage import BaseModel


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.storage = FileStorage()

    def test_creation(self):
        '''
            this test validate that creation proccess was correct.
        '''
        self.assertEqual(self.storage.save(), None)
