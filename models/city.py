"""Module containing the City class"""


from models.base_model import BaseModel


class City(BaseModel):
    """Class that defines a City object"""

    self.name = ""
    self.state_id = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
