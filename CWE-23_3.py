#4.# Code with CWE-23:

import os

filename = input("Enter the name of the file to write: ")
with open(filename, "w") as f:
    f.write("Hello, world!")

# Vulnerable line: Line 3, where user input is accepted without any validation or sanitization.
# Description: This code is vulnerable to CWE-23 (Relative Path Traversal) as it allows an attacker to input a malicious path that can write to any file on the system.