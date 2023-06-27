#10.# CWE-22: Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')

import os

filename = input("Enter file name: ")
path = "/home/user/files/"

if not filename.isalnum() or "../" in filename:
    print("Invalid file name")
else:
    full_path = os.path.join(path, filename)
    with open(full_path, "r") as file:
        print(file.read())