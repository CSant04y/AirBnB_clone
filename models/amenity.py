"""Module Containing the amenity class"""


from models.base_model import BaseModel

class Amenity(BaseModel):
    """Class that defines a State object"""

    def __init__(self):
        super().__init__
        self.name = ""
