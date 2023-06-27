#3.# Command Injection:


import os

filename = input("Enter filename: ")
os.system("cat " + filename)

# The vulnerable line is the os.system call where user input is concatenated directly into the command, allowing for command injection attacks.