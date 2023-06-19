import sqlite3
import hashlib
import socket
import threading
import rsa

#Make an open TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Bind IP
server.bind(("localhost", 9999))
#Open
server.listen()

#Handle Connection
def handle_connection(c):
    c.send("Username: ".encode())
    username = c.recv(1024).decode()
    c.send("Password: ".encode())
    password = c.recv(1024).decode()
    password = hashlib.sha256(password).hexdigest()

    conn = sqlite3.connect("userdata.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM userdata WHERE username = ? AND password = ?", (username, password))

    if cur.fetchall():
        c.send("Login Successful".encode())
    else:
        c.send("Login Failed".encode())