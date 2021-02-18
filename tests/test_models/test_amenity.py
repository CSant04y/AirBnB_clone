#!/usr/bin/python3
"""Module containing unittests for amenity.py"""


import unittest
import datetime
from models.amenity import Amenity
from models import storage
import os


strptime = datetime.datetime.strptime


class TestAmenity(unittest.TestCase):
    """class to test the amenity class and its methods"""

    def setUp(self):
        """Happens before each function"""
        self.test_dict = {"created_at": "2021-02-15T16:06:02.924677",
                          "id": "19b4933a-55d0-4287-99a0-773c1dcab528",
                          "updated_at": "2021-02-15T16:06:02.924677",
                          "__class__": "Amenity", "name": ""}
        self.obj = Amenity(**self.test_dict)

    def test_init(self):
        """This is the Unittest for the init of Amenity"""
        self.assertIsInstance(self.obj, Amenity)
        self.assertEqual(self.obj.id, self.test_dict["id"])
        self.assertEqual(self.obj.created_at,
                         strptime(self.test_dict["created_at"],
                                  '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(self.obj.updated_at,
                         strptime(self.test_dict["updated_at"],
                                  '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(self.obj.created_at, self.obj.updated_at)
        self.assertEqual(self.obj.name, "")
        self.assertIsInstance(self.obj.created_at, datetime.datetime)
        self.assertIsInstance(self.obj.updated_at, datetime.datetime)
        self.assertIsInstance(self.obj.id, str)
        self.assertIsInstance(self.obj.name, str)

        'This is test for else statment'
        self.obj = Amenity()

        self.assertIsInstance(self.obj, Amenity)
        self.assertNotEqual(self.obj.id, "")
        self.assertEqual(self.obj.created_at, self.obj.updated_at)
        self.assertEqual(self.obj.name, "")
        self.assertIsInstance(self.obj.created_at, datetime.datetime)
        self.assertIsInstance(self.obj.updated_at, datetime.datetime)
        self.assertIs(self.obj, storage.objects[type(self.obj).__name__ + "." +
                      str(self.obj.id)])
        self.assertIsInstance(self.obj.id, str)
        self.assertIsInstance(self.obj.name, str)
