#5.# Example 5:


import os

filename = input("Enter a filename: ")
os.system("echo " + filename + " > /dev/null")


# CWE-78: Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')
# Vulnerable line: os.system("echo " + filename + " > /dev/null")
# Description: The user input is concatenated with the "echo" command, allowing for arbitrary command execution.