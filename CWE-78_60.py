#4.# Path traversal vulnerability in Python code:


import os

filename = input("Enter filename: ")

with open(os.path.join('/home/user/files', filename), 'r') as f:
    contents = f.read()

# Vulnerable line: with open(os.path.join('/home/user/files', filename), 'r') as f: