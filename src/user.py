import sys
sys.path.append('/home/anuj/Desktop/droneBase')

import sqlite3
from database.db import conn

class User:
    def __init__(self, id, userName):
        self.id = id 
        self.username = userName

    @classmethod
    def createNew(cls, userName, password):
        cursor = conn.cursor()
        data = None

        try:
            cursor.execute("INSERT INTO users(`username`, `password`) VALUES (?,?);", (userName, password))
            cursor.execute("SELECT `id`, `username` FROM users WHERE `id` = ?", (cursor.lastrowid, ))
            data = cursor.fetchone()

            conn.commit()
        except sqlite3.IntegrityError as err:
            raise Exception('User already exists')
        except Exception as exc:
            print(str(exc))
            raise Exception('Something went wrong')
        finally:
            cursor.close()

        return cls(data[0], data[1])

    @classmethod
    def readAll(cls):
        cursor = conn.cursor()
        data = None
        result = []

        try:
            cursor.execute("SELECT * FROM `users`")
            data = cursor.fetchall()

        except:
            raise Exception ("Something went wrong while getting data")
        finally:
            cursor.close()

        for i in data:
            result.append(cls(i[0], i[1], i[2]))
        return result
        
    @classmethod
    def delete(cls):
        cursor = conn.cursor()

        try:
            cursor.execute("DELETE FROM `users` WHERE id = ?")
            conn.commit()
        except:
            raise Exception("User with this id doesn't exists ")
        finally:
            cursor.close()

    @classmethod
    def update(cls, userName, password):
        cursor = conn.cursor()

        try:
            cursor.execute("UPDATE `users` SET username = ? WHERE id = ?", (userName, ))
            cursor.execute("UPDATE `users` SET password = ? WHERE id = ?", (password, ))
            conn.commit()
        except:
            raise Exception("User with this id doesn't exists ")
        finally:
            cursor.close()


