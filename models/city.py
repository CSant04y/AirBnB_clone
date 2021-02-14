"""Module containing the City class"""


from models.base_model import BaseModel

class City(BaseModel):
    """Class that defines a City object"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = ""
