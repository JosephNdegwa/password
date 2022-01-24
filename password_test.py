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

    self.assertEqual(self.new_User.user_name,"Joseph")
    self.assertEqual(self.new_User.password,"Password")
    self.assertEqual(self.new_User.email,"joseph.ndegwa@student.moringaschool.com")




if __name__ == '__main__':
    unittest.main()