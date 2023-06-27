#3.# Command Injection:


import os

filename = input("Enter filename: ")
os.system("cat " + filename)


# The vulnerable line is line 3, where user input is directly concatenated into the command string, allowing for command injection attacks.