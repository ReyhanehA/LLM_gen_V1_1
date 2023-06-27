#1.# SQL Injection:


import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()

username = input("Enter username: ")
password = input("Enter password: ")

c.execute("SELECT * FROM users WHERE username = '{}' AND password = '{}'".format(username, password))


# The vulnerable line is the SQL query on line 8, where user input is directly concatenated into the query string, allowing for SQL injection attacks.