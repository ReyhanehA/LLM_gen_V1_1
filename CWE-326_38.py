#9.# CWE-326: Insecure Storage of Sensitive Information
# Vulnerable line: db.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
# Description: The password is stored in a database without any encryption or protection, making it vulnerable to theft or unauthorized access.
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="mydatabase",
    user="myusername",
    password="mypassword"
)

cur = conn.cursor()

username = input("Enter username: ")
password = input("Enter password: ")

cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
conn.commit()