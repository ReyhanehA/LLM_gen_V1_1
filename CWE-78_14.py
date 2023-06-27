#5.# Example 5: LDAP Injection

import ldap

username = input("Enter username: ")
password = input("Enter password: ")

conn = ldap.initialize('ldap://localhost')
conn.simple_bind_s(username, password)

# CWE-78: The user input is not properly sanitized and can be used to inject LDAP commands
# Vulnerable line: conn.simple_bind_s(username, password)