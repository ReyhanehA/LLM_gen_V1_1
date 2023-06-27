#6.# CWE-96: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')
# Vulnerable line: cursor.execute("SELECT * FROM users WHERE username='" + user_input + "'")
import sqlite3
conn = sqlite3.connect('users.db')
cursor = conn.cursor()
user_input = input("Enter a username: ")
cursor.execute("SELECT * FROM users WHERE username='" + user_input + "'")
result = cursor.fetchall()
print(result)