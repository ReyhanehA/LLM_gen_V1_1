#1.# SQL Injection vulnerability in Python code:


import sqlite3

username = input("Enter username: ")
password = input("Enter password: ")

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
cursor.execute(query)

# Vulnerable line: query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"

result = cursor.fetchone()

if result:
    print("Login successful")
else:
    print("Invalid credentials")