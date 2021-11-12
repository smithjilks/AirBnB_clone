#!/usr/bin/python3
"""
Module that serializes and deserializes instances to/from JSON files
"""
import json

class FileStorage:
    """Class that serializes instances to a JSON file
    and deserializes JSON file to instances

    Attributes:
         __file_path (str): path to JSON file
         __objects (dict): stors all objects by <class name>.id
    """

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """Initializes the class object"""
        pass

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
        self.__objects[obj_key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            dict_map = {key: value.to_dict()
                    for key, value in self.__objects.items()}
            json.dump(dict_map, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists, otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        try:
            with open(self.__file_path, 'r') as f:
                dict_map = json.load(f)
                dict_map = {key: self.dict()[value["__class__"]](**value)
                        for key, value in dict_map.items()}
                self.__objects = dict_map

        except Exception:
            pass

    def dict(self):
        """
        Returns dict representaion of all the classes
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        return {
            "BaseModel": BaseModel,"Amenity": Amenity,
            "City": City, "Place": Place,
            "Review": Review,"State": State,"User": User
        }
        
