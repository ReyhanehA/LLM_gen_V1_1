#9.# Example 9: Path Traversal

import os

filename = input("Enter filename: ")

with open(os.path.join('/home/user/files', filename), 'r') as f:
    data = f.read()

# Vulnerable line: with open(os.path.join('/home/user/files', filename), 'r') as f:
# Description: This code is vulnerable to path traversal as it allows the user to specify a filename that includes directory traversal characters, which could allow them to access files outside of the intended directory.