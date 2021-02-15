#!/usr/bin/python3
"""Module containing unittests for base_model.py """


import unittest
import datetime
from models.base_model import BaseModel
from models import storage


class TestBaseModel(unittest.TestCase):
    """class to test the Base_Model class and its methods"""

    def test_init(self):
        """This is the Unittest for the init of BaseModel"""
        test_dict = {"created_at": "2021-02-15T19:28:17.168400", "updated_at":
                     "2021-02-15T19:28:17.168428", "id":
                     "7152df91-ec26-4595-bf75-fd84f02a3bd9"}

        obj = BaseModel(**test_dict)

        self.assertIsInstance(obj, BaseModel)
        self.assertEqual(obj.id, test_dict["id"])
        self.assertEqual(obj.created_at, test_dict["created_at"])
        self.assertEqual(obj.updated_at, test_dict["updated_at"])
        self.assertEquals(obj.created_at, obj.updated_at)
        self.assertIsInstance(obj.created_at, datetime.datetime)
        self.assertIsInstance(obj.updated_at, datetime.datetime)
        self.assertIs(obj, storage.objects[type(obj).__name__ + "." +
                      str(obj.id)])
        self.assertIsInstance(obj.id, str)

        'This is test for else statment'
        obj = BaseModel()

        self.assertIsInstance(obj, BaseModel)
        self.assertNotEqual(obj.id, "")
        self.assertEquals(obj.created_at, obj.updated_at)
        self.assertIsInstance(obj.created_at, datetime.datetime)
        self.assertIsInstance(obj.updated_at, datetime.datetime)
        self.assertIs(obj, storage.objects[type(obj).__name__ + "." +
                      str(obj.id)])
        self.assertIsInstance(obj.id, str)

    def test_str(self):
        """[This is the Unittest for __str__ method]
        """
        test_dict = {"created_at": "2021-02-15T19:28:17.168400", "updated_at":
                     "2021-02-15T19:28:17.168428", "id":
                     "7152df91-ec26-4595-bf75-fd84f02a3bd9"}

        obj = BaseModel(**test_dict)

        del obj.created_at
        del obj.updated_at
        self.assertEqual(obj.__str__[:30], 
                         "[BaseModel] (7152df91-ec26-4595-bf75-fd84f02a3bd9)] {")

        self.assertEqual(obj.__str__[-1:], "}")

    def test_to_dict(self):
        """[This Unittest the to_dict method]
        """

    def test_save(self):
        """[This Unittests the save method]
        """
