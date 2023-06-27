#2.# Command Injection:


import os

filename = input("Enter filename: ")

os.system("cat " + filename)

# The vulnerable line is the os.system call where user input is directly concatenated into the command, allowing for command injection attacks.