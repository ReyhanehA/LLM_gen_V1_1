#2.# Example 2:


import os

filename = input("Enter a filename: ")
if os.path.exists(filename):
    with open(filename, "r") as f:
        print(f.read())
else:
    print("File not found.")


# Vulnerable line: line 2
# Description: This code is vulnerable to CWE-284 (Improper Access Control) because it does not properly validate the user's input. An attacker could enter a malicious filename and potentially access sensitive files on the system.