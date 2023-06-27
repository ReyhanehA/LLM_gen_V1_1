#4.# Example 4: Path Traversal

import os

filename = input("Enter filename: ")

# CWE-78: The user input is not properly sanitized and can be used to traverse directories
# Vulnerable line: with open(filename, 'r') as f:
with open(os.path.join('/home/user/files', filename), 'r') as f:
    print(f.read())