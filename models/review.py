"""Module containing the Review class"""


from models.base_model import BaseModel


class Review(BaseModel):
    """Class that defines a Review object"""
    self.place_id = ""
    self.user_id = ""
    self.text = ""
