#10.# Code with CWE-23:

import os

filename = input("Enter the name of the directory to delete: ")
os.rmdir(filename)

# Vulnerable line: Line 3, where user input is accepted without any validation or sanitization.
# Description: This code is vulnerable to CWE-23 (Relative Path Traversal) as it allows an attacker to input a malicious path that can delete any directory on the system.