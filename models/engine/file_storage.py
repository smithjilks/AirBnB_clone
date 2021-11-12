#!/usr/bin/python3
"""
Module that serializes and deserializes instances to/from JSON files
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """Class that serializes instances to a JSON file
    and deserializes JSON file to instances

    Attributes:
         __file_path (str): path to JSON file
         __objects (dict): stors all objects by <class name>.id
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """

        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id

        Args:
            obj (object): object to add to objects
        """

        obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.objects[obj_key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        with open(self.__file_path, 'w+') as f:
            json.dump({key: value.to_dict()
                       for key, value in self.__objects.items()}, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists, otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        try:
            with open(self.__file_path, 'r') as f:
                __objects = json.loads(f.read())

        except Exception:
            pass
