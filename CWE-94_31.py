#3.# Example 3: CWE-94 - Improper Control of Generation of Code ('Code Injection')

import sqlite3

user_input = input("Enter a table name: ")
conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute("SELECT * FROM " + user_input)

# The vulnerable line is c.execute("SELECT * FROM " + user_input)
# This code allows an attacker to inject arbitrary SQL commands into the system by manipulating the user_input variable.