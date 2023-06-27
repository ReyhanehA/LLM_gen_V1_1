#5.# CWE-79: LDAP Injection
# Vulnerable line:
query = "(uid=" + username + ")"
result = ldap.search(base_dn, ldap.SCOPE_SUBTREE, query)

# Description: This code is vulnerable to LDAP injection as it concatenates user input directly into an LDAP query without proper sanitization.