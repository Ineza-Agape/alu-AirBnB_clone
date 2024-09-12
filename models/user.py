#!/usr/bin/python3
"""Creating the User class."""

from models.base_model import BaseModel


class User(BaseModel):
    """The User.
    Attributes:
        email (str): User's email
        password (str): The user's password.
        first_name (str):First name
        last_name (str): Last name 
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
