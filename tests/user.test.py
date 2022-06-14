import sys
sys.path.append('/home/anuj/Desktop/droneBase')

import unittest
from src.user import User
from database.db import conn

# Arrange, Act, Assert
class UserTests(unittest.TestCase):
    def setUp(self):
        conn.execute('delete from users;')
        conn.commit()

    def test_create_new_user(self):
        result = User.createNew("abc", "afaf")
        
        self.assertEqual(result.username, "abc")
        self.assertIsNotNone(result.id)

    def test_error_on_same_username(self):
        result = User.createNew("abc", "afaf")

        try:
            User.createNew("abc", "afaf")
        except Exception as e:
            self.assertEqual(str(e), 'User already exists')

if __name__ == "__main__":
    unittest.main()