import sys
sys.path.append('/home/anuj/Desktop/droneBase')

import sqlite3
import bcrypt

from database.db import conn

class User:
    def __init__(self, username, id = None):
        self.id = id
        self.username = username

    @classmethod
    def createNew(cls, userName, password):
        cursor = conn.cursor()
        data = None

        try:
            hashedPassword = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

            cursor.execute("INSERT INTO users(`username`, `password`) VALUES (?,?);", (userName, hashedPassword.decode()))
            cursor.execute("SELECT `id`, `username` FROM users WHERE `id` = ?", (cursor.lastrowid, ))
            data = cursor.fetchone()

            conn.commit()
        except sqlite3.IntegrityError:
            raise Exception('User already exists')
        except Exception as exc:
            print(str(exc))
            raise Exception('Something went wrong')
        finally:
            cursor.close()

        return cls(id=data[0], username=data[1])

    @classmethod
    def findByUsername(cls, username):
        cursor = conn.cursor()
        data = None

        try:
            cursor.execute("SELECT `id`, `username` FROM users WHERE `username` = ? limit 1", (username, ))
            data = cursor.fetchone()
        except Exception as e:
            raise Exception("Something went wrong")
        finally:
            cursor.close()

        if data is None:
            raise Exception('User not found')
        
        return cls(id=data[0], username=data[1])

    @classmethod
    def readAll(cls):
        cursor = conn.cursor()
        data = None
        result = []

        try:
            cursor.execute("SELECT id, username FROM `users`")
            data = cursor.fetchall()

        except:
            raise Exception ("Something went wrong while getting data")
        finally:
            cursor.close()

        for i in data:
            result.append(cls(id=i[0], username=i[1]))
        return result

    @classmethod
    def delete(cls, id):
        cursor = conn.cursor()

        try:
            cursor.execute("DELETE FROM `users` WHERE id = ?", (id, ))
            conn.commit()
        except:
            raise Exception("User with this id doesn't exists ")
        finally:
            cursor.close()

    @classmethod
    def update(cls, id, username = None, password = None):
        cursor = conn.cursor()

        try:
            if username is not None:
                cursor.execute("UPDATE `users` SET username = ? WHERE id = ?", (username, id))
            if password is not None:
                hash_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

                cursor.execute("UPDATE `users` SET password = ? WHERE id = ?", (hash_password.decode(), id))
            
            conn.commit()
        except:
            raise Exception("User with this id doesn't exists ")
        finally:
            cursor.close()

    def checkPassword(self, password):
        query = 'select id, password from users where username = ? limit 1;'

        cursor = conn.cursor()
        cursor.execute(query, (self.username, ))

        data = cursor.fetchone()
        
        if (data is None):
            raise Exception("User not found")

        self.id = data[0]
        userPassword = data[1]
        
        return bcrypt.checkpw(password.encode('utf-8'), userPassword.encode('utf-8'))