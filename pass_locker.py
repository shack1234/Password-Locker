#!/usr/bin/env python3.6
import pyperclip
from user import User, Credential


def create_user(fullname, username, password):
    """
	Function to create a new user account
	"""
    new_user = User(fullname, username, password)
    return new_user
