import unittest
from password import User


def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_User = User("Joseph","Password","joseph.ndegwa@student.moringaschool.com")



def test_init(self):
    '''
    test_init test case to test if the object is initialized properly
    '''