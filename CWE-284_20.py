#1.# Example 1: CWE-284 - Improper Access Control

import os

file_path = "/path/to/file"
if os.path.exists(file_path):
    with open(file_path, "r") as f:
        print(f.read())

# The vulnerable line is line 4 where the code reads a file without checking if the user has permission to access it.