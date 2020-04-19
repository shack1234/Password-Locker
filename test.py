import unittest # Importing the unittest module
from user import User,Credential # Importing the user class

class TestUser(unittest.TestCase):
	'''
	Test class that defines test cases for the user class behaviours.

	Args:
		unittest.TestCase: TestCase class that helps in creating test cases
	''' 
	def tearDown(self):
		'''
		tearDown method that does clean up after each test case has run.
		'''
		User.user_list = []
		
	def setUp(self):
		'''
		Set up method to run before each test cases.
		'''
		self.new_user = User("shadrack","maestro","s1234") # create user object
	def test_init(self):
		'''
		test_init test case to test if the object is initialized properly
		'''
		self.assertEqual(self.new_user.fullname,"shadrack")
		self.assertEqual(self.new_user.username,"maestro")
		self.assertEqual(self.new_user.password,"s1234")
		
	def test_save_users(self):
		'''
		test_save_users test case to test if the users object is saved into
			the user list
		'''
		self.new_user.save_users() # saving the new users
		self.assertEqual(len(User.user_list),1)
	def test_save_multiple_users(self):
		
		'''
		test_save_multiple_users to check if we can save multiple users
		objects to our user_list
		'''
		self.new_user.save_users()
		test_user = User("Test","user","password") # new users
		test_user.save_users()
		self.assertEqual(len(User.user_list),2)
			
	#end of class user
		
class TestCredentials(unittest.TestCase):
	'''
	Test class that defines test cases for the credentials class behaviours.
	Args:
		unittest.TestCase: helps in creating test cases
	'''
	def test_check_user(self):
		'''
		Function to test whether the login in function check_user works as expected
		'''
		self.new_user = User('shadrack','maestro','s1234')
		self.new_user.save_users()
		addUser = User('','','') # test if another user will be added 
		addUser.save_users()

		for user in User.user_list:
			if user.username == addUser.username and user.password == addUser.password:
				current_user = user.username
		return current_user

		self.assertEqual(current_user,Credential.check_user(addUser.password,addUser.username))
	def tearDown(self):
		'''
		tearDown method that does clean up after each test case has run.
		'''
		Credential.cred_list = []


	def setUp(self):
		'''
		Set up method to run before each test cases.
		'''
		self.new_credential = Credential('shadrack','Facebook','s1234')

	def test__init__(self):
		'''
		Test to  check if the initialization/creation of credential instances is properly done
		'''
		self.assertEqual(self.new_credential.user_name,'shadrack')
		self.assertEqual(self.new_credential.site_name,'Facebook')
		self.assertEqual(self.new_credential.password,'s1234')

	def test_save_credentials(self):
		'''
		Test to check if the new credential info is saved into the credentials list
		'''
		self.new_credential.save_credentials()
		twitter = Credential('shadrack','Twitter','s1234')
		twitter.save_credentials()
		self.assertEqual(len(Credential.cred_list),2)
    
    #testing testing
	def test_user_name_exists(self):
		'''
		test to check if we can return a Boolean  if we cannot find the sitename.
		'''
	@classmethod
	def user_name_exist(cls,user_name):
		'''
		Method that checks if a user name exists from the cred list.
		Args:
			user_namae: user name to  search if it exists
		Returns :
			Boolean: True or false depending if the site exists
		'''
		self.new_credential.save_credentials()
		test_user_name = Credential("user","site","pass") # new cred
		test_user_name.save_credentials()

		user_name_exists = Credential.user_name_exist("user")

		self.assertTrue(user_name_exists)
		
		for cred in cls.cred_list:
			if cred.user_name == user_name:
					return True

		return False
	
	def test_copy_password(self):
			'''
		Test to confirm that we are copying the password 
		'''
	@classmethod
	def copy_password(cls,password):
		pass_found = Credential.find_by_sitename(site_name)
		pyperclip.copy(pass_found.password)
		
		self.new_contact.save_contact()
		Credential.copy_password("1234")

		self.assertEqual(self.new_user.password,pyperclip.paste())
	


	def test_delete_credential(self):
		"""
		test method to test if we can remove an account credentials from our cred_list
		"""
		self.new_credential.save_credentials()
		test_credential = Credential("user","site","pass")
		test_credential.save_credentials()

		self.new_credential.delete_credentials()
		self.assertEqual(len(Credential.cred_list),1)
		#testing
	
	def test_find_credential(self):
		"""
		test to check if we can find a credential entry by account name and display the details of the credential
		"""
		self.new_credential.save_credentials()
		test_credential = Credential("user","site","pass") 
		test_credential.save_credentials()

		credential = Credential.find_credential("user")

		self.assertEqual(credential.user_name,test_credential.user_name)

	def test_credential_exist(self):
		"""
		test to check if we can return a true or false based on whether we find or can't find the credential.
		"""
		self.new_credential.save_credentials()
		credential = Credential("user", "site", "pass")  
		credential.save_credentials()
		credential_is_found = Credential.if_credential_exist("user")
		self.assertTrue(credential_is_found)

	

if __name__ == '__main__':
	unittest.main()