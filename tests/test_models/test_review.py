#!/usr/bin/python3
"""Module containing unittests for review.py"""


import unittest
import datetime
from datetime.datetime import strptime as strptime
from models.review import Review
from models import storage
import os


class TestReview(unittest.TestCase):
    """class to test the Review class and its methods"""

    def setUp(self):
        """Happens before each function"""
        self.test_dict = {"created_at": "2021-02-15T16:06:14.339688",
                          "id": "ac984526-613a-4ec8-933d-ab32a5f924b9",
                          "place_id": "",
                          "updated_at": "2021-02-15T16:06:14.339688",
                          "__class__": "Review", "text": "", "user_id": ""}
        self.obj = Review(**self.test_dict)

    def test_init(self):
        """This is the Unittest for the init of Review"""
        self.assertIsInstance(self.obj, Review)
        self.assertEqual(self.obj.id, self.test_dict["id"])
        self.assertEqual(self.obj.created_at,
                         strptime(self.test_dict["created_at"],
                                  '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(self.obj.updated_at,
                         strptime(self.test_dict["updated_at"],
                                  '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(self.obj.created_at, self.obj.updated_at)
        self.assertEqual(self.obj.place_id, "")
        self.assertEqual(self.obj.user_id, "")
        self.assertEqual(self.obj.text, "")
        self.assertIsInstance(self.obj.created_at, datetime.datetime)
        self.assertIsInstance(self.obj.updated_at, datetime.datetime)
        self.assertIsInstance(self.obj.id, str)
        self.assertIsInstance(self.obj.place_id, str)
        self.assertIsInstance(self.obj.user_id, str)
        self.assertIsInstance(self.obj.text, str)

        'This is test for else statment'
        self.obj = Review()

        self.assertIsInstance(self.obj, Review)
        self.assertNotEqual(self.obj.id, "")
        self.assertEqual(self.obj.created_at, self.obj.updated_at)
        self.assertEqual(self.obj.place_id, "")
        self.assertEqual(self.obj.user_id, "")
        self.assertEqual(self.obj.text, "")
        self.assertIsInstance(self.obj.created_at, datetime.datetime)
        self.assertIsInstance(self.obj.updated_at, datetime.datetime)
        self.assertIs(self.obj, storage.objects[type(self.obj).__name__ + "." +
                      str(self.obj.id)])
        self.assertIsInstance(self.obj.id, str)
        self.assertIsInstance(self.obj.place_id, str)
        self.assertIsInstance(self.obj.user_id, str)
        self.assertIsInstance(self.obj.text, str)
