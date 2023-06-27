#8.# Example 8: LDAP Injection

import ldap

conn = ldap.initialize('ldap://localhost')
conn.simple_bind_s('cn=' + username + ',dc=example,dc=com', password)

# The vulnerable line is line 3 where user input is concatenated into an LDAP query
# CWE-20: Improper Input Validation
# This code is vulnerable to LDAP injection attacks as it does not properly sanitize user input