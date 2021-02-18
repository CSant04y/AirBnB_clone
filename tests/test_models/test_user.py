#!/usr/bin/python3
"""Module containing unittests for user.py"""


import unittest
import datetime
from models.user import User
from models import storage
import os


strptime = datetime.datetime.strptime


class TestUser(unittest.TestCase):
    """class to test the User class and its methods"""

    def setUp(self):
        """Happens before each function"""
        self.test_dict = {"created_at": "2021-02-15T16:05:26.603170",
                          "id": "bf654f25-d81f-4d02-a3c0-1777c5bfeda5",
                          "updated_at": "2021-02-15T16:05:26.603170",
                          "__class__": "User", "first_name": "",
                          "password": "", "last_name": "", "email": ""}
        self.obj = User(**self.test_dict)

    def test_init(self):
        """This is the Unittest for the init of User"""
        self.assertIsInstance(self.obj, User)
        self.assertEqual(self.obj.id, self.test_dict["id"])
        self.assertEqual(self.obj.created_at,
                         strptime(self.test_dict["created_at"],
                                  '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(self.obj.updated_at,
                         strptime(self.test_dict["updated_at"],
                                  '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(self.obj.created_at, self.obj.updated_at)
        self.assertEqual(self.obj.first_name, "")
        self.assertEqual(self.obj.last_name, "")
        self.assertEqual(self.obj.email, "")
        self.assertEqual(self.obj.password, "")
        self.assertIsInstance(self.obj.created_at, datetime.datetime)
        self.assertIsInstance(self.obj.updated_at, datetime.datetime)
        self.assertIsInstance(self.obj.id, str)
        self.assertIsInstance(self.obj.first_name, str)
        self.assertIsInstance(self.obj.last_name, str)
        self.assertIsInstance(self.obj.email, str)
        self.assertIsInstance(self.obj.password, str)

        'This is test for else statment'
        self.obj = User()

        self.assertIsInstance(self.obj, User)
        self.assertNotEqual(self.obj.id, "")
        self.assertEqual(self.obj.created_at, self.obj.updated_at)
        self.assertEqual(self.obj.first_name, "")
        self.assertEqual(self.obj.last_name, "")
        self.assertEqual(self.obj.email, "")
        self.assertEqual(self.obj.password, "")
        self.assertIsInstance(self.obj.created_at, datetime.datetime)
        self.assertIsInstance(self.obj.updated_at, datetime.datetime)
        self.assertIs(self.obj, storage.objects[type(self.obj).__name__ + "." +
                      str(self.obj.id)])
        self.assertIsInstance(self.obj.id, str)
        self.assertIsInstance(self.obj.first_name, str)
        self.assertIsInstance(self.obj.last_name, str)
        self.assertIsInstance(self.obj.email, str)
        self.assertIsInstance(self.obj.password, str)
