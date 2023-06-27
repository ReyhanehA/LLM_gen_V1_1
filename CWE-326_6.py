#7.# CWE-326: Insecure Storage of Sensitive Information
# Vulnerable line: conn = psycopg2.connect(database="mydb", user="myuser", password="mypassword", host="localhost", port="5432")
# Description: The PostgreSQL database is created without any encryption or protection, making it vulnerable to theft or unauthorized access.

import psycopg2
conn = psycopg2.connect(database="mydb", user="myuser", password="mypassword", host="localhost", port="5432")