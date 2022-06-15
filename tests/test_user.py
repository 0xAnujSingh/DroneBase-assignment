import sys
from turtle import update
sys.path.append('/home/anuj/Desktop/droneBase')

import unittest
import bcrypt

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

class UserQueryTests(unittest.TestCase):
    def setUp(self):
        username = 'test_user'
        password = 'secret'
        hash_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        conn.execute("delete from users")
        conn.execute("insert into users(`username`, `password`) values(?, ?)", (username, hash_password))
        conn.commit()

    def test_user_not_exists(self):
        try:
            result = User.findByUsername("abc")
        except Exception as err:
            self.assertEqual(str(err), "User not found")

    def test_user_exists(self):
        result = User.findByUsername("test_user")
        self.assertEqual(result.username, "test_user")


class UserCheckPasswordTests(unittest.TestCase):
    def setUp(self):
        username = 'test_user'
        password = 'secret'
        hash_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        conn.execute("delete from users")
        conn.execute("insert into users(`username`, `password`) values(?, ?)", (username, hash_password))
        conn.commit()

    def test_check_password(self):
        user = User(username='test_user')

        password_match = user.checkPassword('secret')

        self.assertEqual(password_match, True)


    def test_incorrect_password(self):
        user = User(username='test_user')

        password_match = user.checkPassword('not_secret')

        self.assertEqual(password_match, False)

    def test_invalid_user(self):
        try:
            user = User(username='does_not_exist')
            user.checkPassword('not_secret')
        except Exception as err:
            self.assertEqual(str(err), 'User not found')

class UserReadAllTests(unittest.TestCase):
    def setUp(self):
        conn.execute("delete from users")
       

    def test_read_all(self):
        password = 'secret'
        hash_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
        first_user = 'test_user'
        second_user = 'sec_user'
        conn.execute("insert into users(`username`, `password`) values(?, ?)", (first_user, hash_password))
        conn.execute("insert into users(`username`, `password`) values(?, ?)", (second_user, hash_password))
        conn.commit()

        result = User.readAll()
        self.assertEqual(len(result), 2)

if __name__ == "__main__":
    unittest.main()

