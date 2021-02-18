#!/usr/bin/python3
"""[This File contains Class User]
"""

from models.base_model import BaseModel


class User(BaseModel):
    """[This class inherits from BaseModel and has\
    infroamtion on user]

    Args:
        BaseModel ([Super class]): [The base class]
    """
    self.email = ""
    self.password = ""
    self.first_name = ""
    self.last_name = ""
