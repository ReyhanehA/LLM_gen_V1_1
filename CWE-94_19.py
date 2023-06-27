#1.# Example 1: SQL Injection

import sqlite3

username = input("Enter username: ")
password = input("Enter password: ")

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
cursor.execute(query)

# Vulnerable line: query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
# Description: This code is vulnerable to SQL injection as it concatenates user input directly into the SQL query without proper sanitization.