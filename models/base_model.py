#!/usr/bin/python3
"""[This is the Class Base Model]
"""

import uuid
import datetime


class BaseModel:
    """[This is the Class BaseModel]
    """

    def __init__(self, *args, **kwargs):
        """[This instatiates the public instance attributes]
        """
        from models import storage
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        self.__dict__[key] = datetime.datetime.strptime(
                                kwargs[key], '%Y-%m-%dT%H:%M:%S.%f')
                    else:
                        self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """[This id the string representation of [Class] (id) dictonary]
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     str(self.__dict__))

    def to_dict(self):
        """[]
        """
        temp_dict = self.__dict__.copy()
        temp_dict["created_at"] = temp_dict["created_at"].isoformat()
        temp_dict["updated_at"] = temp_dict["updated_at"].isoformat()
        temp_dict["__class__"] = type(self).__name__
        return temp_dict

    def save(self):
        """[summary]
        """
        from models import storage
        self.updated_at = datetime.datetime.now()
        storage.save()

    @property
    def objects(self):
        """[Getter for __objects to avoid name mangling]
        """
        return self.__objects

    @objects.setter
    def objects(self, new_dict):
        """[Setter for __objects so we can do unittests]
        """
        self.__objects = new_dict

    @property
    def file_path(self):
        """[getter for File path]
        """
        return(self.__file_path)

    @file_path.setter
    def file_path(self, file):
        """[File Path setter idk]
        """
        self.__file_path = file
