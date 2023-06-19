import sqlite3
import hashlib

#Connect to userdata.db
conn = sqlite3.connect("userdata.db")
cur = conn.cursor()

#Create Table
cur.execute("""
CREATE TABLE IF NOT EXISTS userdata (
    id INTEGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
)
""")

#Echo in samples
username1, password1 = "john", hashlib.sha256("johnpassword".encode()).hexdigest()
username2, password2 = "badbunny", hashlib.sha256("forwardsdoim".encode()).hexdigest()
username3, password3 = "jaiden", hashlib.sha256("roldsolid".encode()).hexdigest()
username4, password4 = "skinwalker", hashlib.sha256("badpass".encode()).hexdigest()
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username1, password1))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username2, password2))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username3, password3))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username4, password4))

#Commit
conn.commit()