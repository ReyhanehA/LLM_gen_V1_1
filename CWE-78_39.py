#10.# Example 10:


import os

filename = input("Enter a filename: ")
os.system("touch " + filename)


# CWE-78: Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')
# Vulnerable line: os.system("touch " + filename)
# Description: The user input is concatenated with the "touch" command, allowing for arbitrary file creation.