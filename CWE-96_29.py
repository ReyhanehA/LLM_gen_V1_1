#1.# SQL Injection:


import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()

username = input("Enter username: ")
password = input("Enter password: ")

c.execute("SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'")

# The vulnerable line is the SQL query where user input is concatenated directly into the query, allowing for SQL injection attacks.