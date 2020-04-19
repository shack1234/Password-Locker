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

def delete_credential(self):
    """
    Function to delete a Credentials from credentials list
    """
    credentials.delete_credentials()


def main():
    print(" ")
    print(" Hello! Welcome to Password Locker.")
    while True:
        print(" ")
        print("*" * 50)
        print(
            "Use this shortcuts to choose your tasks: \n 1-Create an Account \n 2-Log In \n 3-Exit"
        )
        short_code = input("Choose your task: ").lower().strip()
        if short_code == "3":
            print("~" * 52)
            print("Thanks for using Password Locker")
            print("~" *52)
            break
        elif short_code == "1":
            print("*" * 50)
            print(" ")
            print("To create a new account:")
            fullname = input("Enter your fullname: ").strip()
            username = input("Enter your username :").strip()
            print(" ")
            print(
              "Please choose an option for entering a password:\n1-Create your own password\n2-Use Random generated password"
            )
            psw_choice = input("Choose your option:").lower().strip()
            print("*" *35)
            if psw_choice == "1":
                print(" ")
                password = input("Enter your password: ").strip()
                
            elif psw_choice == "2":
                password = generate_password()
                
            else:
                print("Oops! Something went wrong. Try again.")
            save_users(create_user(fullname, username, password))
            print(" ")
            print(
                f"\nNew Account Created for:\t\nFullname:{fullname }\nUsername:{username}\npassword:{password}"
            )
       
