#1.# Example 1: SQL Injection

import sqlite3

username = input("Enter username: ")
password = input("Enter password: ")

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
cursor.execute(query)

# CWE-78: The user input is not properly sanitized and can be used to inject SQL commands
# Vulnerable line: query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"