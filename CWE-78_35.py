#6.# Example 6:


import os

filename = input("Enter a filename: ")
os.system("rm -rf " + filename)


# CWE-78: Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')
# Vulnerable line: os.system("rm -rf " + filename)
# Description: The user input is concatenated with the "rm" command and the "-rf" flag, allowing for arbitrary file deletion.