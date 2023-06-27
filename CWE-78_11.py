#2.# Example 2: Command Injection

import os

filename = input("Enter filename: ")

# CWE-78: The user input is not properly sanitized and can be used to inject commands
# Vulnerable line: os.system("cat " + filename)
os.system("cat " + filename)