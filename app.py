import sqlite3
from db import conn

class Users:
    def __init__(self, userName, password):
        self.id = id
        self.userName = userName
        self.password = password

        def show(self):
            print(self.userName)

Users().show()



    @classmethod
    def createNew(cls, userName, password):
        cursor = conn.cursor()
        data = None

        try:
            cursor.execute("INSERT INTO users(`user_name`, `passsword`) VALUES (?,?);", (userName, password))
            cursor.execute("SELECT `id`, `user_name` FROM users WHERE `id` = ?", (cursor.lastrowid, ))
            data = cursor.fetchone()

            conn.commit()
        except:
            raise Exception("Account already exists")
        finally:
            cursor.close()

        return cls(data[0], data[1], data[2])

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
            cursor.execute("UPDATE `users` SET user_name = ? WHERE id = ?", (userName, ))
            cursor.execute("UPDATE `users` SET password = ? WHERE id = ?", (password, ))
            conn.commit()
        except:
            raise Exception("User with this id doesn't exists ")
        finally:
            cursor.close()


