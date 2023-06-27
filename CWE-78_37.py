#8.# Example 8:


import os

filename = input("Enter a filename: ")
os.system("cp " + filename + " /tmp/")


# CWE-78: Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')
# Vulnerable line: os.system("cp " + filename + " /tmp/")
# Description: The user input is concatenated with the "cp" command, allowing for arbitrary file copying.