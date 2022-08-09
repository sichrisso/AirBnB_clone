#!/usr/bin/env python3
"""
Place module
This module have and manage Place Entity
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Public class attributes:
        city_id (str): empty string: it will be the City.id
        user_id (str): empty string: it will be the User.id
        name (str): empty string
        description (str): empty string
        number_rooms (int): 0
        number_bathrooms (int): 0
        max_guest (int): 0
        price_by_night (int): 0
        latitude (float): 0.0
        longitude (float): 0.0
        amenity_ids (list): empty str list, it will be the list of Amenity.id
    """
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        if len(kwargs) == 0:
            super().__init__()

        # if kwargs have values
        if len(kwargs) > 0:
            super().__init__(**kwargs)
