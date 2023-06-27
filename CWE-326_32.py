#3.# CWE-326: Insecure Storage of Sensitive Information
# Vulnerable line: db.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
# Description: The password is stored in a database without any encryption or protection, making it vulnerable to theft or unauthorized access.
import sqlite3

conn = sqlite3.connect('example.db')
db = conn.cursor()

username = input("Enter username: ")
password = input("Enter password: ")

db.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
conn.commit()