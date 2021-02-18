#!/usr/bin/python3
"""Module containing unittests for place.py"""


import unittest
import datetime
from models.place import Place
from models import storage
import os


strptime = datetime.datetime.strptime


class TestPlace(unittest.TestCase):
    """class to test the Place class and its methods"""

    def setUp(self):
        """Happens before each function"""
        self.test_dict = {"created_at": "2021-02-15T16:05:47.103874",
                          "latitude": 0.0, "longitude": 0.0,
                          "updated_at": "2021-02-15T16:05:47.103874",
                          "amenity_ids": [], "city_id": "", "number_rooms": 0,
                          "id": "52cf288d-f402-4564-a91f-06c71004c6b7",
                          "name": "", "number_bathrooms": 0, "description": "",
                          "price_by_night": 0, "user_id": "", "max_guest": 0,
                          "__class__": "Place"}
        self.obj = Place(**self.test_dict)

    def test_init(self):
        """This is the Unittest for the init of Place"""
        self.assertIsInstance(self.obj, Place)
        self.assertEqual(self.obj.id, self.test_dict["id"])
        self.assertEqual(self.obj.created_at,
                         strptime(self.test_dict["created_at"],
                                  '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(self.obj.updated_at,
                         strptime(self.test_dict["updated_at"],
                                  '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(self.obj.created_at, self.obj.updated_at)
        self.assertEqual(self.obj.latitude, 0.0)
        self.assertEqual(self.obj.longitude, 0.0)
        self.assertEqual(self.obj.city_id, "")
        self.assertEqual(self.obj.user_id, "")
        self.assertEqual(self.obj.name, "")
        self.assertEqual(self.obj.description, "")
        self.assertEqual(self.obj.number_rooms, 0)
        self.assertEqual(self.obj.number_bathrooms, 0)
        self.assertEqual(self.obj.price_by_night, 0)
        self.assertEqual(self.obj.max_guest, 0)
        self.assertEqual(self.obj.amenity_ids, [])
        self.assertIsInstance(self.obj.created_at, datetime.datetime)
        self.assertIsInstance(self.obj.updated_at, datetime.datetime)
        self.assertIsInstance(self.obj.id, str)
        self.assertIsInstance(self.obj.latitude, float)
        self.assertIsInstance(self.obj.longitude, float)
        self.assertIsInstance(self.obj.city_id, str)
        self.assertIsInstance(self.obj.user_id, str)
        self.assertIsInstance(self.obj.name, str)
        self.assertIsInstance(self.obj.description, str)
        self.assertIsInstance(self.obj.number_rooms, int)
        self.assertIsInstance(self.obj.number_bathrooms, int)
        self.assertIsInstance(self.obj.price_by_night, int)
        self.assertIsInstance(self.obj.max_guest, int)
        self.assertIsInstance(self.obj.amenity_ids, list)

        'This is test for else statment'
        self.obj = Place()

        self.assertIsInstance(self.obj, Place)
        self.assertNotEqual(self.obj.id, "")
        self.assertEqual(self.obj.created_at, self.obj.updated_at)
        self.assertEqual(self.obj.latitude, 0.0)
        self.assertEqual(self.obj.longitude, 0.0)
        self.assertEqual(self.obj.city_id, "")
        self.assertEqual(self.obj.user_id, "")
        self.assertEqual(self.obj.name, "")
        self.assertEqual(self.obj.description, "")
        self.assertEqual(self.obj.number_rooms, 0)
        self.assertEqual(self.obj.number_bathrooms, 0)
        self.assertEqual(self.obj.price_by_night, 0)
        self.assertEqual(self.obj.max_guest, 0)
        self.assertEqual(self.obj.amenity_ids, [])
        self.assertIsInstance(self.obj.created_at, datetime.datetime)
        self.assertIsInstance(self.obj.updated_at, datetime.datetime)
        self.assertIsInstance(self.obj.created_at, datetime.datetime)
        self.assertIsInstance(self.obj.updated_at, datetime.datetime)
        self.assertIs(self.obj, storage.objects[type(self.obj).__name__ + "." +
                      str(self.obj.id)])
        self.assertIsInstance(self.obj.id, str)
        self.assertIsInstance(self.obj.id, str)
        self.assertIsInstance(self.obj.latitude, float)
        self.assertIsInstance(self.obj.longitude, float)
        self.assertIsInstance(self.obj.city_id, str)
        self.assertIsInstance(self.obj.user_id, str)
        self.assertIsInstance(self.obj.name, str)
        self.assertIsInstance(self.obj.description, str)
        self.assertIsInstance(self.obj.number_rooms, int)
        self.assertIsInstance(self.obj.number_bathrooms, int)
        self.assertIsInstance(self.obj.price_by_night, int)
        self.assertIsInstance(self.obj.max_guest, int)
        self.assertIsInstance(self.obj.amenity_ids, list)
