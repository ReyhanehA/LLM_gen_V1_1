#3.# Code with CWE-78: Path Traversal

import os

filename = input("Enter filename: ")
path = "/home/user/files/" + filename
with open(path, 'r') as f:
    data = f.read()

# Vulnerable line: path = "/home/user/files/" + filename
# Description: This code is vulnerable to path traversal as it concatenates user input directly into the file path without proper validation or sanitization.