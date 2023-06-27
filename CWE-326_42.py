#3.# CWE-326: Insecure Storage of Sensitive Information
# Vulnerable line: db.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
# Description: User passwords are stored in a database without any encryption or hashing, making them vulnerable to theft.
import sqlite3
conn = sqlite3.connect('users.db')
db = conn.cursor()
username = input("Enter your username: ")
password = input("Enter your password: ")
db.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
conn.commit()