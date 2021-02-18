"""Module containing the Review class"""


from models.base_model import BaseModel


class Review(BaseModel):
    """Class that defines a Review object"""
    place_id = ""
    user_id = ""
    text = ""
