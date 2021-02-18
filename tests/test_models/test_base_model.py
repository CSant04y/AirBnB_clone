#!/usr/bin/python3
"""Module containing unittests for base_model.py """


import unittest
import datetime
from datetime.datetime import strptime as strptime
from models.base_model import BaseModel
from models import storage
import os


class TestBaseModel(unittest.TestCase):
    """class to test the Base_Model class and its methods"""

    def setUp(self):
        """Happens before each function"""
        self.test_dict = {"created_at": "2021-02-15T19:28:17.168400",
                          "updated_at":
                          "2021-02-15T19:28:17.168400",
                          "id": "7152df91-ec26-4595-bf75-fd84f02a3bd9"}
        self.obj = BaseModel(**self.test_dict)

    def test_init(self):
        """This is the Unittest for the init of BaseModel"""
        self.assertIsInstance(self.obj, BaseModel)
        self.assertEqual(self.obj.id, self.test_dict["id"])
        self.assertEqual(self.obj.created_at,
                         strptime(self.test_dict["created_at"],
                                  '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(self.obj.updated_at,
                         strptime(self.test_dict["updated_at"],
                                  '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertIsInstance(self.obj.created_at, datetime.datetime)
        self.assertIsInstance(self.obj.updated_at, datetime.datetime)
        self.assertIsInstance(self.obj.id, str)

        'This is test for else statment'
        self.obj = BaseModel()

        self.assertIsInstance(self.obj, BaseModel)
        self.assertNotEqual(self.obj.id, "")
        self.assertEqual(self.obj.created_at, self.obj.updated_at)
        self.assertIsInstance(self.obj.created_at, datetime.datetime)
        self.assertIsInstance(self.obj.updated_at, datetime.datetime)
        self.assertIs(self.obj, storage.objects[type(self.obj).__name__ + "." +
                      str(self.obj.id)])
        self.assertIsInstance(self.obj.id, str)

    def test_str(self):
        """[This is the Unittest for __str__ method]
        """
        test_str = self.obj.__str__()
        self.assertEqual(test_str[:52],
                         "[BaseModel] \
                         (7152df91-ec26-4595-bf75-fd84f02a3bd9) {")
        self.assertEqual(test_str[-1:], '}')

    def test_to_dict(self):
        """[This Unittest the to_dict method]
        """
        obj2 = BaseModel(**self.test_dict)
        obj_dict = self.obj.to_dict()
        self.assertDictEqual(self.obj.__dict__, obj2.__dict__)
        self.assertEqual(obj_dict["id"],
                         "7152df91-ec26-4595-bf75-fd84f02a3bd9")
        self.assertEqual(obj_dict["created_at"], "2021-02-15T19:28:17.168400")
        self.assertEqual(obj_dict["updated_at"], "2021-02-15T19:28:17.168400")
        self.assertEqual(obj_dict["__class__"], "BaseModel")
        self.assertIsInstance(obj_dict["id"], str)
        self.assertIsInstance(obj_dict["created_at"], str)
        self.assertIsInstance(obj_dict["updated_at"], str)
        self.assertIsInstance(obj_dict["__class__"], str)

    def test_save(self):
        """[This Unittests the save method]
        """
        self.obj.save()
        now_ish = datetime.datetime.now()
        time = datetime.datetime.strftime(self.obj.__dict__["updated_at"],
                                          '%Y-%m-%dT%H:%M:%S')
        self.assertEqual(time, datetime.datetime.strftime(now_ish,
                                                          '%Y-%m-%dT%H:%M:%S'))
