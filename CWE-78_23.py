#4.# Example 4:

import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()

username = input("Enter a username: ")
password = input("Enter a password: ")

c.execute("INSERT INTO users (username, password) VALUES ('" + username + "', '" + password + "')")

# CWE-78: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')
# Vulnerable line: c.execute("INSERT INTO users (username, password) VALUES ('" + username + "', '" + password + "')")
# Description: The user input for username and password can be manipulated to execute arbitrary SQL commands.