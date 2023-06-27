#9.# Example 9:


import os

filename = input("Enter a filename: ")
os.system("mv " + filename + " /tmp/")


# CWE-78: Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')
# Vulnerable line: os.system("mv " + filename + " /tmp/")
# Description: The user input is concatenated with the "mv" command, allowing for arbitrary file moving.