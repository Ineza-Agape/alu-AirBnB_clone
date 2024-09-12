#!/usr/bin/python3
"""Defining Review class."""

from models.base_model import BaseModel


class Review(BaseModel):
    """Representing a review.
    Attributes:
    place_id (str): The unique identifier for the place.
    user_id (str): The unique identifier for the user who wrote the review.
    text (str): The content of the review.
    """


    place_id = ""
    user_id = ""
    text = ""
