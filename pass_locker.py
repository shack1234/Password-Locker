#!/usr/bin/env python3.6
import pyperclip
from user import User, Credential


def create_user(fullname, username, password):
    """
	Function to create a new user account
	"""
    new_user = User(fullname, username, password)
    return new_user

def save_users(user):
    """
	Function to save a new user account
	"""
    User.save_users(user)


def verify_user(username, password):
    """
	Function that verifies the existance of the user before creating credentials
	"""
    checking_user = Credential.check_user(username, password)
    return checking_user

def generate_password():
    """
	Function to generate a password automatically
	"""
    random_pass = Credential.generate_password()
    return random_pass


def create_credential(user_name, site_name, password):
    """
	Function to create a new credential
	"""
    new_credential = Credential(user_name, site_name, password)
    return new_credential


def save_credentials(credential):
    """
	Function to save a newly created credential
	"""
    Credential.save_credentials(credential)


def display_credentials(user_name):
    """
	Function to display credentials saved by a user
	"""
    return Credential.display_credentials(user_name)


def copy_credential(password):
    """
	Function to copy a credentials details to the clipboard
	"""
    return Credential.copy_credential(site_name)
    #testing 

def find_credential(user_name):
    """
    Function that finds a Credentials by an account name and returns the Credentials that belong to that account
    """
    return Credential.find_credential(user_name)
