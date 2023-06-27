#3.# Command injection vulnerability in Python code:


import os

filename = input("Enter filename: ")

os.system("cat " + filename)

# Vulnerable line: os.system("cat " + filename)