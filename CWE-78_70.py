#4.# Path Traversal:


import os

filename = input("Enter filename: ")
with open(os.path.join('/home/user/files', filename), 'r') as f:
    print(f.read())


# The vulnerable line is line 3, where user input is directly concatenated into the file path without proper validation, allowing for path traversal attacks.