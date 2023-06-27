#2.# Example 2:


import os

filename = input("Enter a filename: ")
os.system("rm " + filename)


# CWE-78: Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')
# Vulnerable line: os.system("rm " + filename)
# Description: The user input is concatenated with the "rm" command, allowing for arbitrary command execution.