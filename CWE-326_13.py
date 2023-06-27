#4.# CWE-326: Insecure Storage of Sensitive Information
# Vulnerable line: conn.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
# Description: The user's password is stored in a database without any encryption or protection, making it vulnerable to theft or unauthorized access.
import sqlite3

conn = sqlite3.connect("users.db")
username = "user1"
password = "password123"
conn.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
conn.commit()