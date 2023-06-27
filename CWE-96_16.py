#7.# CWE-96: Improper Neutralization of Directives in Statically Saved Code (XSS)

import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()

name = input("Enter a name: ")
age = input("Enter an age: ")

c.execute("INSERT INTO users (name, age) VALUES ('" + name + "', " + age + ")")

# The vulnerable line is line 7 where user input is directly concatenated with a SQL query without proper sanitization, allowing for potential SQL injection attacks.