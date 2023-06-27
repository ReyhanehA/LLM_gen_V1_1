#7.# Example 7: Path Traversal

import os

filename = input("Enter a filename: ")
with open(os.path.join('/home/user/files', filename), 'r') as f:
    print(f.read())

# The vulnerable line is line 3 where user input is directly used in a file path without proper sanitization.
# CWE-20: Improper Input Validation