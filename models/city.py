#!/usr/bin/python3
"""Defining the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Representing a city.
    Attributes:
        STATE_id (str): The state id.
        NAME (str): The name of the city.
    """

    STATE_id = ""
    NAME = ""
