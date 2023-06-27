#2.# Example 2:

import os

filename = input("Enter a filename: ")
os.system("rm " + filename)

# CWE-78: Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')
# Vulnerable line: os.system("rm " + filename)
# Description: The user input for filename can be manipulated to execute arbitrary commands.