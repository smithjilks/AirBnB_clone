#!/usr/bin/python3
"""
This model contains a unit test class for the BaseModel class
"""
import unittest
import pycodestyle
from models import storage
from models.base_model import BaseModel
from datetime import datetime


class TestBaseClass(unittest.TestCase):
    """
    BaseModel test class
    """

    def setUp(self):
        """
        Initializes BaseModel instances
        """
        self.bm1 = BaseModel()
        self.bm2 = BaseModel()

    def test_pep8_compliance(self):
        """
        Tests compliance of the class with pep8
        """
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_save(self):
        """
        Tests save method works as expected
        """
        self.before_save = self.bm1.updated_at
        self.bm1.save()
        self.assertNotEqual(self.bm1.updated_at, self.before_save)

    def test_to_dict(self):
        """
        Test to_dict method works as expected
        """
        self.bm1_dict = dict(self.bm1.__dict__)
        self.bm1_dict['__class__'] = "BaseModel"
        self.bm1_dict['created_at'] = self.bm1_dict['created_at'].isoformat()
        self.bm1_dict['updated_at'] = self.bm1_dict['updated_at'].isoformat()

        self.assertDictEqual(self.bm1_dict, self.bm1.to_dict())

    def test_create_from_dict(self):
        """
        Tests that BaseModel creates an instance from kwargs
        and that the created instance is not the same as previous instance
        from which the kwargs were created from
        """
        self.bm = BaseModel()
        self.bm1_json = self.bm1.to_dict()
        self.bm_from_dict = BaseModel(**self.bm1_json)
        self.assertNotEqual(self.bm, self.bm_from_dict)

    def test_uuid_type(self):
        """
        Tests that the id assigned to the instance is of type string
        """
        self.assertEqual(str, type(self.bm1.id))


if __name__ == '__main__':
    unittest.main()
