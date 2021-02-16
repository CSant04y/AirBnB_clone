"""Module Containing the amenity class"""


from models.base_model import BaseModel

class Amenity(BaseModel):
    """Class that defines a State object"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = ""