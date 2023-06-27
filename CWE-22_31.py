#1.# Example 1: CWE-22 - Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')

import os

filename = input("Enter file name: ")
path = "/home/user/files/"

if "../" in filename:
    print("Invalid file name")
else:
    full_path = os.path.join(path, filename)
    with open(full_path, "r") as f:
        print(f.read())

# The vulnerable line is line 6 where the input is not properly validated and allows for directory traversal attacks.