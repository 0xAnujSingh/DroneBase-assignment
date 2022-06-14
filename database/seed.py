import sqlite3

conn = sqlite3.connect('droneBase.db')

conn.execute(''' CREATE TABLE IF NOT EXISTS users (
    id integer primary key autoincrement not null,
    username varchar(120) not null unique,
    password varchar(255) not null
)  
''')

conn.commit()

conn.close()