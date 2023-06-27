#2.# Example 2: SQL Injection

import sqlite3

username = input("Enter your username: ")
password = input("Enter your password: ")

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

query = "SELECT * FROM users WHERE username = '{}' AND password = '{}'".format(username, password)
cursor.execute(query)

if cursor.fetchone():
    print("Login successful.")
else:
    print("Invalid username or password.")

conn.close()

# The vulnerable line is line 8 where user input is directly used in a SQL query without proper sanitization.
# CWE-20: Improper Input Validation