#!/usr/bin/env python3
'''This module contains a base class called 'BaseModel'that defines all common
attributes/methods for other classes.
'''
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Public instance attributes:
        id (str):  assign with an uuid when an instance is created.
        created_at: current datetime when an instance is created
        updated_at: current datetime when an instance is created and it will
        be updated every time the object changes.
    """

    def __init__(self, *args, **kwargs):
        """ constructor for initialization of BaseModel and  validate kwargs
        Args:
             *args(any): unused
             **kwargs(dict):key/value pairs
        """
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                setattr(self, key, value)

            self.created_at = datetime.strptime(
                self.created_at, '%Y-%m-%dT%H:%M:%S.%f')
            self.updated_at = datetime.strptime(
                self.updated_at, '%Y-%m-%dT%H:%M:%S.%f')

    def __str__(self):
        """Overriding the __str__ method
        Returns:
            Information with this format:
            [<class name>] (<self.id>) <self.__dict__>
        """
        my_dict = self.__dict__

        my_dict['updated_at'] = self.updated_at
        my_dict['created_at'] = self.created_at

        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id,
                                         my_dict)

    def save(self):
        """updates the public instance attribute updated_at with the
        current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns:
            -A dictionary containing keys/values of __dict__ of the instance
            -A 'key __class__'  with the class name of the object.
            -'created_at' and 'updated_at' in isoformat()
        """
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__

        if type(self.updated_at) is datetime:
            my_dict['updated_at'] = self.updated_at.isoformat()

        if type(self.created_at) is datetime:
            my_dict['created_at'] = self.created_at.isoformat()

        return my_dict
