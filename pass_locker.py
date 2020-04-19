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
        elif short_code == "2":
            print("*" * 50)
            print("To Login, Enter your account details:")
            username = input("Enter your username : ").strip()
            password = str(input("Enter your password : "))
            user_exists = verify_user(username, password)
            if user_exists == username:
                print("~"*52)
                print(f"Welcome {username}.Please choose an option to continue.")
                print("~"*52)
                while True:
                    print("*" * 50)
                    print(
                        "Use this shortcuts to choose your tasks:\n1-Create a Credential\n2-Display Credentials\n3-Login\n4-Delete Credential\n5-Exit"
                    )
                    short_code = input("Choose your task: ").lower().strip()
                    print("*" * 50)
                    if short_code == "5":
                        print("~"*30)
                        print(f"Goodbye  {username}")
                        print("~"* 30)
                        break
                    elif short_code == "1":
                        print(" ")
                        print("Enter your credential details:")
                        user_name = input("Enter the username: ").strip()
                        site_name = input("Enter your site name :").strip()
                        while True:
                            print(" ")
                            print("*" * 50)
                            print(
                                "Please choose an option for entering a password:\n1-Create your own password\n2-Use Random generated password\n3-Exit"
                            )
                            psw_choice = input("Choose your task: ").lower().strip()
                            print("*" * 50)
                            if psw_choice == "1":
                                print(" ")
                                password = input("Enter your password: ").strip()
                                break
                            elif psw_choice == "2":
                                password = generate_password()
                                break
                            elif psw_choice == "3":
                                break
                            else:
                                print("Oops! Something went wrong. Try again.")
                        save_credentials(
                            create_credential(user_name, site_name, password)
                        )
                        print(" ")
                        print(
                            f"\nCredential Created:\nUsername:{user_name}\nSite Name:{site_name}\nPassword:{password}"
                        )
                        print(" ")
                    elif short_code == "2":
                        print("~"* 50)
                        if display_credentials(user_name):
                            print("Your credentials")
                            for credential in display_credentials(user_name):
                                print(
                                    f"\nSite Name:{credential.site_name}\nUsername:{credential.user_name} \nPassword:{credential.password}"
                                )
                            print("~"*50)
                        else:
                            print(" ")
                            print("You don't seem to have any credentials saved yet")
                            print(" ")
                    elif short_code == "3":
                        print("*" * 50)
                        print(" ")
                        print("To Login, Enter your account details:")
                        user_name = input("Enter your username : ").strip()
                        password = str(input("Enter your password : "))
                        user_cred_exists = verify_user(user_name, password)
                        if user_cred_exists == user_name:

                            print(" ")
                            print(f"Welcome  to {site_name}")
                            print(" ")
                    if short_code == "4":
                        print("To Delete a Credentials :")
                        search_name = input("Enter your username : ").strip()
                        if find_credential(search_name):
                            search_credential = find_credential(search_name)
                            print("_"*50)
                            search_credential.delete_credentials()
                            print('\n')
                            print(f"Credential for {search_credential.user_name} has been successfully deleted!!!")
                            print('\n')
                        else:
                            print("No credential saved.Add a credential first and Try again")
            else:
                print(" ")
                print("Oops! Wrong details entered. Try again or Create an Account.")
        else:
            print("*" * 50)
            print(" ")
            print("Oops! Something went wrong!. Try again.")


if __name__ == "__main__":
    main()


           
