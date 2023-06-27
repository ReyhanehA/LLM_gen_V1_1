#6.# CWE-326: Insecure Storage of Sensitive Information
# Vulnerable line: db.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
# Description: The password is stored in a database without any encryption or protection, making it vulnerable to theft or unauthorized access.
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

username = input("Enter username: ")
password = input("Enter password: ")

mycursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
mydb.commit()