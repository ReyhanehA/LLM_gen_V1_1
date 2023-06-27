#4.# Example 4:


import sqlite3

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

username = input("Enter a username: ")
password = input("Enter a password: ")

query = "SELECT * FROM users WHERE username='{}' AND password='{}'".format(username, password)
cursor.execute(query)

if cursor.fetchone() is not None:
    print("Login successful!")
else:
    print("Invalid username or password.")


# CWE-284: Improper Access Control
# The vulnerable line is line 8, where user input is directly used to construct an SQL query without proper validation. An attacker can use this to perform SQL injection attacks.