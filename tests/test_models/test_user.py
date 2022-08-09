#!/usr/bin/python3
"""
    This is a module test from BaseModel class and your methods.
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """
    this class test user class and your behavior
    """

    def setUp(self):
        self.user = User()

    def test_creation(self):
        '''this test validate that creation proccess was correct.
        '''

        data = {'id' : 3,
            'fist_name' : 'Betty',
            'last_name':'Holberton',
            'password':'123',
            'email':'correo@correo',
            }

        self.user = User(**data)
        self.assertEqual(self.user.id, 3)
        self.assertEqual(self.user.first_name, 'Betty')
        self.assertEqual(self.user.first_name, 'Holberton')
        self.assertEqual(self.user.password, '123')
        self.assertEqual(self.user.email, 'correo@correo')
