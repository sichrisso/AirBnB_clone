#!/usr/bin/env python3
"""This module contains a class called 'Amenity'that inherits from 'BaseModel'
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Public class attributes:
        name: string - empty string
    """
    name = ''

    def __init__(self, *args, **kwargs):
        if len(kwargs) == 0:
            super().__init__()

        # if kwargs have values
        if len(kwargs) > 0:
            super().__init__(**kwargs)
