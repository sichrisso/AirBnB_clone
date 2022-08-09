#!/usr/bin/env python3
"""This module contains a base class called 'FileStorage' that defines
the process that serializes and deserializes to JSON

file_storage module manages data stored in file.json
and manages CRUD operation
"""
import json
import importlib
import re


class FileStorage:
    """ An abstracted file storage engine
    Private class attributes:
        __file_path: string - path to the JSON file (ex: file.json)
        __objects: dictionary - empty but will store all objects by
        class name.id

    Public instance methods:
        all(self): returns the dictionary __objects
        new(self, obj): sets in __objects the obj with
        key <obj class name>.id save(self): serializes
        __objects to the JSON file (path: __file_path)
        reload(self): deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists otherwise
        , do nothing.
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """Creates a new instance of a specific class and
        saves it into the file storage
        """
        key_name = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key_name] = obj

    def save(self):
        """Saves the instances of all classes into a
        .json file using the json string format
        """
        content = self.__serialize()

        with open(FileStorage.__file_path, 'w') as file:
            file.write(content)

    def reload(self):
        """Deserializes the JSON file to __objects (only if
        the JSON file (__file_path) exists ; otherwise, do nothing.
        """
        file_data = self.__deserialize()

        if not file_data:
            return

        for k, value in file_data.items():
            class_name = value["__class__"]
            FileStorage.__objects[k] = self.choose_class(class_name, value)

    def create(self, class_name):
        """Auxiliar function to create new instances of an specific class
        """
        my_model = self.choose_class(class_name)
        my_model.save()
        print(my_model.id)

    def choose_class(self, class_name, data=None):
        """Chooses the correct kind of class for an instance - to create
        instances, to use the to_dict function, to save into the Json file,etc.
        """
        module_name = self.to_snake_case(class_name)
        module = importlib.import_module(module_name)
        class_ = getattr(module, class_name)
        if data:
            return class_(**data)
        else:
            return class_()

    def print(self, class_name=None):
        """ print all elements in storage and filter by class_name"""
        print(self.filter_by_class(class_name))

    def filter_by_class(self, class_name):
        """Auxiliar function to print or show the instances of an specific
        type of class.
        """
        if not class_name:
            return self.to_list()

        filtered = []
        for k, value in self.all().items():
            split_key = k.split('.')
            if split_key[0] == class_name:
                filtered.append(str(value))
        return filtered

    def to_list(self):
        """ take a dictionary and transform this to list
            with objects cast to str"""
        data_list = []
        for _, value in self.all().items():
            data_list.append(str(value))
        return data_list

    def __serialize(self):
        """
        BaseModel->to_dict() -> <class 'dict'> -> JSON dump -> <class 'str'>
        """
        objects = {}
        for key, obj in self.all().items():
            objects[key] = obj.to_dict()

        return str(json.dumps(objects))

    def __deserialize(self):
        "File -> str -> JSON load -> dict -> BaseModel"
        try:
            with open(FileStorage.__file_path) as file:
                return json.load(file)
        except:
            pass

    def to_snake_case(self, text):
        """ Transform text to snake case """
        module_name = re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()
        return "models.{}".format(module_name)
