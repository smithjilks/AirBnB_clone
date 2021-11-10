#!/usr/bin/python3
"""
Module containing a base class from which other classes wiil inherit
"""


from uuid import uuid4
from datetime import datetime

class BaseModel:
    """Base class from which other classes will inherit from

    Attributes:
          id(str): uuid
          created_at: timestamp of the creation day of the class
          updated_at: timestamp of the update day of the class
    """

    def __init__(self):
        """Initializes the class object
        """
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        """
        Updates updated_at with modification date timestamp
        """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """
        Returns a dict containing all keys/values of __dict__ of the instance
        """
        dict_map = {}
        for k, v in self.__dict__.items():
            if k == "created_at" or k == "updated_at":
                dict_map[k] = v.isoformat()
            else:
                dict_map[k] = v
        dict_map["__class__"] = self.__class__.__name__

        return dict_map

    def __str__(self):
        return "[{}] ({}) <{}>".format(self.__class__.__name__, self.id,
                                       self.__dict__ )
