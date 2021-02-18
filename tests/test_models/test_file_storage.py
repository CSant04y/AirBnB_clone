#!/usr/bin/python3
"""This is the Unitest for file_storage.py"""

import unittest
import copy
import os
import json
from models.__init__ import dict_of_classes
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """This is Unittest for the method FileStorage"""

    def setUp(self):
        """This is the setup method for Unittesting"""
        self.otter = FileStorage()
        self.otter.file_path = "test_file.json"
        self.otter.reload()
        self.objects = self.otter.objects
        self.UrchinA = self.objects["Amenity.\
19b4933a-55d0-4287-99a0-773c1dcab528"]
        self.UrchinB = self.objects["BaseModel.\
7152df91-ec26-4595-bf75-fd84f02a3bd9"]
        self.UrchinC = self.objects["City.\
f76cbf19-eb40-4901-88ca-569684490fd1"]
        self.UrchinP = self.objects["Place.\
52cf288d-f402-4564-a91f-06c71004c6b7"]
        self.UrchinR = self.objects["Review.\
ac984526-613a-4ec8-933d-ab32a5f924b9"]
        self.UrchinS = self.objects["State.\
125b2cf3-66d9-4185-b442-e8a49cb7801d"]
        self.UrchinU = self.objects["User.\
bf654f25-d81f-4d02-a3c0-1777c5bfeda5"]

    def test_all(self):
        """This is the Unittest for the method all"""
        test_dict = self.otter.all()
        self.assertIsInstance(test_dict, dict)
        for key in test_dict:
            self.assertEqual(test_dict[key], self.otter.objects[key])

    def test_new(self):
        """This is a Unittest for the method new"""
        new_obj = copy.deepcopy(self.UrchinB)
        new_obj.id = "7152df91-ec26-4595-bf75-fd84f02atest"
        self.otter.new(new_obj)
        otter_dict = self.otter.objects
        test_obj = otter_dict["BaseModel.7152df91-ec26-4595-bf75-fd84f02atest"]
        self.assertIsInstance(test_obj, BaseModel)
        self.assertEqual(test_obj.id, "7152df91-ec26-4595-bf75-fd84f02atest")

    def test_save(self):
        """This is a Unittest for the the method save"""
        if os.path.isfile("test_save.json"):
            os.remove("test_save.json")
        self.otter.reload()
        self.otter.file_path = "test_save.json"
        self.otter.save()
        with open(self.otter.file_path, "r") as FILE:
            test_save_dict = json.loads(FILE.read())
        with open("test_file.json", "r") as FILE:
            test_file_dict = json.loads(FILE.read())
        self.assertDictEqual(test_save_dict, test_file_dict)
        os.remove("test_save.json")

    def test_reload(self):
        """This is a Unittest for the method reload"""
