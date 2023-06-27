#7.# Example 7:


import os

filename = input("Enter a filename: ")
os.system("chmod 777 " + filename)


# CWE-78: Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')
# Vulnerable line: os.system("chmod 777 " + filename)
# Description: The user input is concatenated with the "chmod" command and the "777" permission, allowing for arbitrary file permission changes.