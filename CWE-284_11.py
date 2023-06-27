#2.# Example 2:


import os

filename = input("Enter a filename: ")
if os.path.exists(filename):
    with open(filename, "r") as f:
        print(f.read())
else:
    print("File not found.")


# CWE-284: Improper Access Control
# The vulnerable line is line 2, where the user input is used to construct a file path without proper validation. An attacker can use this to read arbitrary files on the system.