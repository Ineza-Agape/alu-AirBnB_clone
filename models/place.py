#!/usr/bin/python3
"""Defining Place class."""

from models.base_model import BaseModel


class Place(BaseModel):
    """""Representing the place.
    Attributes:
        city_id (str): Identifier for the city where the place is located.
        user_id (str): Identifier for the user who owns or manages the place.
        name (str): The name or title of the place.
        description (str): A brief description of the place.
        number_rooms (int): The total number of rooms in the place.
        number_bathrooms (int): The total number of bathrooms in the place.
        max_guest (int): The maximum number of guests that the place can accommodate.
        price_by_night (int): The cost of staying at the place per night.
        latitude (float): The geographical latitude of the place.
        longitude (float): The geographical longitude of the place.
        amenity_ids (list): A list containing the IDs of available amenities at the place.
    """

    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
