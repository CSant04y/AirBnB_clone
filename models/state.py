"""Module containing the State class"""


from models.base_model import BaseModel

class State(BaseModel):
    """Class that defines a State object"""

    def __init__(self):
        super().__init__
        self.name = ""
