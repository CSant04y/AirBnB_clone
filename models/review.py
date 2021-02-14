"""Module containing the Review class"""


from models.base_model import BaseModel

class Review(BaseModel):
    """Class that defines a Review object"""

    def __init__(self):
        super().__init__
        self.place_id = ""
        self.user_id = ""
        self.text = ""
