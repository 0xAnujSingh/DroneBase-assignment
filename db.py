import sqlite3

conn = sqlite3.connect('droneBase.db')

conn.execute(''' CREATE TABLE IF NOT EXISTS users (
    id integer primary key autoincrement not null,
    user_name varchar(120) not null,
    password varchar(120) not null
)  
''')

conn.commit()

conn.close()