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
