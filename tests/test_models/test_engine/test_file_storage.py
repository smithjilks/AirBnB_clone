#!/usr/bin/python3
"""
This model contains a unit test class for the BaseModel class
"""
import os
import unittest
import pycodestyle
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorageClass(unittest.TestCase):
    """
    FileStorage test class
    """

    def setUp(self):
        """
        Initializes BaseModel instances
        """
        self.bm = BaseModel()

    def test_pep8_compliance(self):
        """
        Tests compliance of the class with pep8
        """
        test_fs = 'tests/test_models/test_engine/test_file_storage.py'
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/engine/file_storage.py',
                                    test_fs])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_all(self):
        """
        Tests all the objects are of dict type
        """
        self.assertEqual(type(storage.all()), dict)

    def test_new(self):
        """
        Tests whether the new method adds object to all objects
        """
        all_objects = storage.all().copy()
        storage.new(BaseModel())
        self.assertNotEqual(all_objects, storage.all())

    def test_save(self):
        """
        Tests whether the save method serializes objects to json file
        """
        os.remove('file.json')
        base_model = BaseModel()
        base_model.save()
        self.assertTrue(os.path.isfile('file.json'))

    def test_reload(self):
        """
        Tests whether the reload method deserializes objects from json file
        """
        all_objects = storage.all().copy()
        all_objects = all_objects.values()
        storage.new(BaseModel())
        storage.reload()
        self.assertEqual(type(all_objects), type(storage.all().values()))

    def test_dict(self):
        """
        Tests that the dict method returns a dict
        """
        classes_dict = storage.dict()
        self.assertEqual(type(classes_dict), dict)


if __name__ == '__main__':
    unittest.main()
