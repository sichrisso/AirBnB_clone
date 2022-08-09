#!/usr/bin/env python3
"""
State module
this module have and manage State Entity
"""
from models.base_model import BaseModel


class State(BaseModel):
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
