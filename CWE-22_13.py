#3.# Example 3: CWE-22 - Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')

import os

filename = input("Enter file name: ")
path = "/home/user/files/"

if not os.path.isfile(os.path.join(path, filename)):
    print("File does not exist")
else:
    full_path = os.path.join(path, filename)
    with open(full_path, "r") as file:
        print(file.read())

# The vulnerable line is line 6 where the input is not properly validated and allows for directory traversal attacks.