#8.# CWE-326: Insecure Storage of Sensitive Information
# Vulnerable line: conn.execute("UPDATE users SET password = '{}' WHERE username = '{}'".format(new_password, username))
# Description: The user's password is updated in a database without any encryption or protection, making it vulnerable to theft or unauthorized access.
import sqlite3

conn = sqlite3.connect("users.db")
username = "user1"
new_password = "new_password123"
conn.execute("UPDATE users SET password = '{}' WHERE username = '{}'".format(new_password, username))
conn.commit()