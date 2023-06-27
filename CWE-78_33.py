#4.# Example 4:


import os

filename = input("Enter a filename: ")
os.system("cat " + filename)


# CWE-78: Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')
# Vulnerable line: os.system("cat " + filename)
# Description: The user input is concatenated with the "cat" command, allowing for arbitrary file reading.