#!/usr/bin/python3
"""[This is the Class Base Model]
"""

import models import storage
import uuid
import datetime

class BaseModel:
    """[This is the Class BaseModel]
    """

    def __init__(self, *args, **kwargs):
        """[This instatiates the public instance attributes]
        """
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        self.__dict__[key] = datetime.datetime.strptime(kwargs[key], '%Y-%m-%dT%H:%M:%S.%f')
                    else:
                        self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self):
        """[This id the string representation]

        Returns:
            [type]: [description]
        """
        return "[{}] ({}) {}".format(type(self), self.id, str(self.__dict__))

    def to_dict(self):
        """[summary]
        """
        return {"id": self.id, "created_at": self.created_at.isoformat(),
                "updated_at": self.updated_at.isoformat(),
                "__class__": type(self).__name__}

    def save(self):
        """[summary]
        """
        self.updated_at = datetime.datetime.now()
        storage.save()
