import pyperclip
import random
import string

global  user_list
class User:
    """
    Class that generates new instances of user.
    """
    user_list = [] # Empty user list

    def __init__(self,fullname,username,password):
        # docstring removed for simplicity
        self.fullname = fullname
        self.username = username
        self.password = password
    # Init method up here
    
    def save_users(self):
        '''
        save_users method saves userss objects into user_list
        '''
        User.user_list.append(self)
        
    @classmethod
    def display_users(cls):
        '''
        method that returns the users list
        '''
        return cls.user_list
        self.assertEqual(User.display_users(), User.user_list)

  
        #Another class
class Credential:
	'''
	Class to create  account credentials, generate passwords and save their information
	'''
	# Class Variables
	cred_list =[]   #creating credentitial list
	cred_library_list = [] # save credentials here
	@classmethod
	def check_user(cls,username,password):
		'''
		Method that checks if the name and password entered match entries in the users_list
		'''
		current_user = ''
		for user in User.user_list:
			if (user.username == username and user.password == password):
				current_user = user.username
		return current_user

	def __init__(self,user_name,site_name,password):
		'''
		Method to define the properties for each user object will hold.
		'''
		# instance variables
		self.user_name = user_name
		self.site_name = site_name
		self.password = password

	def save_credentials(self):
		'''
		Function to save a newly created user instance
		'''
		Credential.cred_list.append(self)
	
	def generate_password(size=10, char=string.ascii_uppercase+string.ascii_uppercase+string.digits):
		'''
		Function to generate 10 character password for a credential
		'''
		random_pass=''.join(random.choice(char) for _ in range(size))
		return random_pass

	@classmethod
	def display_credentials(cls,user_name):
		'''
		Class method to display the list of credentials saved
		'''
		cred_library_list = []
		for credential in cls.cred_list:
			if credential.user_name == user_name:
				cred_library_list.append(credential)
		return cred_library_list
				

	
	@classmethod
	def find_by_site_name(cls, site_name):
		'''
		Method that takes in a site_name and returns a credential that matches that site_name.
		'''
		for credential in cls.cred_list: 
			if credential.site_name == site_name:
				return credential

	@classmethod
	def copy_credential(cls,password):
		'''
		Class method that copies a credential's info after the credential's site name is entered
		'''
		find_credential = Credential.find_by_site_name(password)
		return pyperclip.copy(find_credential.password)       

	def delete_credentials(self):
		"""
		delete_credentials method that deletes an account credentials from the credentials_list
		"""
		Credential.cred_list.remove(self)
	
	@classmethod
	def find_credential(cls, user_name):
		"""
		Method that takes in a account_name and returns a credential that matches that account_name.
		"""
		for credential in cls.cred_list:
			if credential.user_name == user_name:
				return credential
	# @classmethod
	# def copy_password(cls,account):
	#     found_credentials = Credentials.find_credential(account)
	#     pyperclip.copy(found_credentials.password)

	@classmethod
	def if_credential_exist(cls, user_name):
		"""
		Method that checks if a credential exists from the credential list and returns true or false depending if the credential exists.
		"""
		for credential in cls.cred_list:
			if credential.user_name == user_name:
				return True
		return False
