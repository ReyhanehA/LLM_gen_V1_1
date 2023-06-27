#1.# SQL Injection:


import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()

username = input("Enter username: ")
password = input("Enter password: ")

c.execute("SELECT * FROM users WHERE username = '{}' AND password = '{}'".format(username, password))

# The vulnerable line is the SQL query where user input is directly concatenated into the query, allowing for SQL injection attacks.