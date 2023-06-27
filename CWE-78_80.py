#4.# Path Traversal:


import os

filename = input("Enter filename: ")

with open(os.path.join('/home/user/files', filename), 'r') as f:
    print(f.read())

# The vulnerable line is the os.path.join call where user input is directly concatenated into the file path, allowing for path traversal attacks.