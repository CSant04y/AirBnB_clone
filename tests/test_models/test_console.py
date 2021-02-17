#!/usr/bin/python3
"""Module containing unittests for base_model.py """


import unittest
import json
import os
import sys
from unittest.mock import patch
from io import StringIO
import models.engine.file_storage as file_storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class TestBaseModel(unittest.TestCase):
    """class to test the Base_Model class and its methods"""

    def tearDownModule():
        'Might have to delete file'

    def test_all(self):
        """Tests for the all method of Base_Model"""
        self.assertEquals()

    def test_new(self):
        """Tests for the new method of Base_Model"""

    def test_save(self):
        """Tests for the save method of Base_Model"""

    def test_reload(self):
        """Tests for the reload method of Base_Model"""

    def setUpModule():
        """[This sets up a fake json string and dict]
        """
