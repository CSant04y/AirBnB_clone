"""Module containing the State class"""


from models.base_model import BaseModel
import datetime


class State(BaseModel):
    """Class that defines a State object"""

    self.name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

