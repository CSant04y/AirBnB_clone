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
        """[This Converts our dict into a dictonary that is able to be used by json]
        """
        temp_dict = self.__dict__.copy()
        temp_dict["created_at"] = temp_dict["created_at"].isoformat()
        temp_dict["updated_at"] = temp_dict["updated_at"].isoformat()
        temp_dict["__class__"] = type(self).__name__
        return temp_dict

    def save(self):
        """[This updates and adds new information as well as updating the updated_at]
        """
        from models import storage
        self.updated_at = datetime.datetime.now()
        storage.save()
