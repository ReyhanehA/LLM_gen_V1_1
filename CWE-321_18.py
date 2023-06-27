#9.# CWE-321: Use of Hard-coded Database Credentials
# Vulnerable line: db_username = "myusername"
import mysql.connector
cnx = mysql.connector.connect(user=db_username, password="mypassword", host="localhost", database="mydatabase")