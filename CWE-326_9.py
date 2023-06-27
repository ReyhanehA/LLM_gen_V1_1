#10.# CWE-326: Insecure Storage of Sensitive Information
# Vulnerable line: password = getpass.getpass("Enter your password: ")
# Description: The password entered by the user is stored in a variable in plain text, making it vulnerable to theft or unauthorized access.

import getpass
password = getpass.getpass("Enter your password: ")