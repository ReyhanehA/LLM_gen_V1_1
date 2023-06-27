#2.# Code with CWE-78: OS Command Injection

import os

filename = input("Enter filename: ")
os.system("cat " + filename)

# Vulnerable line: os.system("cat " + filename)
# Description: This code is vulnerable to OS command injection as it concatenates user input directly into the command without proper sanitization or validation.