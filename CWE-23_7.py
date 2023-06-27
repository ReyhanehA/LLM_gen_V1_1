#8.# Code with CWE-23:

import os

filename = input("Enter the name of the file to rename: ")
new_filename = input("Enter the new name of the file: ")
os.rename(filename, new_filename)

# Vulnerable line: Line 3 and 4, where user input is accepted without any validation or sanitization.
# Description: This code is vulnerable to CWE-23 (Relative Path Traversal) as it allows an attacker to input a malicious path that can rename any file on the system.