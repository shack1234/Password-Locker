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
		
