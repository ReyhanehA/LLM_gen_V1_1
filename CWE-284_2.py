#3.# CWE-284: Improper Access Control
# Vulnerable line: if user_role in ['admin', 'superuser']:
# Description: This code does not properly restrict access to privileged roles.
if user_role in ['admin', 'superuser']:
    grant_privileged_access()