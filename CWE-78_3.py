#4.# Code with CWE-78: LDAP Injection

import ldap

username = input("Enter username: ")
password = input("Enter password: ")

conn = ldap.initialize('ldap://localhost')
conn.simple_bind_s(username, password)

# Vulnerable line: conn.simple_bind_s(username, password)
# Description: This code is vulnerable to LDAP injection as it passes user input directly into the LDAP bind function without proper sanitization or validation.