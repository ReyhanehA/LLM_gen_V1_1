#4.# Example 4:


import sqlite3

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

username = input("Enter your username: ")
password = input("Enter your password: ")

query = "SELECT * FROM users WHERE username = '{}' AND password = '{}'".format(username, password)
cursor.execute(query)

if cursor.fetchone() is not None:
    print("Access granted!")
else:
    print("Access denied!")


# Vulnerable line: line 7
# Description: This code is vulnerable to CWE-284 (Improper Access Control) because it uses string formatting to construct a SQL query, which can be exploited by an attacker to perform SQL injection attacks.