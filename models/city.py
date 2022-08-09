#!/usr/bin/env python3
"""This module contains a class called 'City'that inherits from 'BaseModel'
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Public class attributes:
        state_id: string - empty string: it will be the State.id
        name: string - empty string
    """
    state_id = ''
    name = ''

    def __init__(self, *args, **kwargs):
        if len(kwargs) == 0:
            super().__init__()

        # if kwargs have values
        if len(kwargs) > 0:
            super().__init__(**kwargs)
