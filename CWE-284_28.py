#9.# Example 9: CWE-284 - Improper Access Control

import sqlite3

db_path = "/path/to/database.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# The vulnerable line is line 3 where the code connects to a SQLite database without checking if the user has permission to access it.