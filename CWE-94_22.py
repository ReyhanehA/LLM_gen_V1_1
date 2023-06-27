#4.# Example 4: Path Traversal

import os

filename = input("Enter filename: ")

with open(os.path.join('/home/user/files', filename), 'r') as f:
    contents = f.read()

# Vulnerable line: with open(os.path.join('/home/user/files', filename), 'r') as f:
# Description: This code is vulnerable to path traversal as it allows the user to specify a file path that is outside of the intended directory.