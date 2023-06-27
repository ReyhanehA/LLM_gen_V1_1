#1.# CWE-284: Improper Access Control
# Vulnerable line: if user_role == 'admin':
# Description: This code does not properly check the user's role before granting access to admin privileges.
if user_role == 'admin':
    grant_admin_privileges()