#2.# Example 2: Command Injection

import os

filename = input("Enter filename: ")

os.system("cat " + filename)

# Vulnerable line: os.system("cat " + filename)
# Description: This code is vulnerable to command injection as it concatenates user input directly into a shell command without proper sanitization.