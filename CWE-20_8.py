#3.# Example 3: Command Injection

import os

filename = input("Enter a filename: ")
os.system("cat {}".format(filename))

# The vulnerable line is line 3 where user input is directly used in a system command without proper sanitization.
# CWE-20: Improper Input Validation