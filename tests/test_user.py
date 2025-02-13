import unittest
from app.models import User

class UserModelTest(unittest.TestCase):
    
    def setUp(self):
        self.new_user = User(password = 'banana')
        
    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)
        
    def test_no_access_password(self): # confirms that our application raises an attributeerror when we try and access the password property.
        
        with self.assertRaises(AttributeError):
            self.new_user.password
            
    def test_password_verification(self): # confirms that our password_hash can be verified when we pass in the correct password.
        
        self.assertTrue(self.new_user.verify_password('banana'))