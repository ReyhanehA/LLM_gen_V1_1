#2.# Example 2: Unvalidated Input

import os

filename = input("Enter filename: ")

if os.path.exists(filename):
    with open(filename, 'r') as f:
        data = f.read()

# Vulnerable line: if os.path.exists(filename):
# Description: This code is vulnerable to unvalidated input as it does not check if the user input is a valid filename before attempting to open it.