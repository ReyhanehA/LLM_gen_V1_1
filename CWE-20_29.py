#4.# Example 4: CWE-20 - Improper Input Validation

import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()

table_name = input("Enter a table name: ")
c.execute("SELECT * FROM " + table_name)

# The vulnerable line is line 5, where the input is not validated and can potentially allow for accessing unintended tables.