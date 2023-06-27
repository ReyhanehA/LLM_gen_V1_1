#5.# Example 5:


import subprocess

command = input("Enter a command: ")
subprocess.call(command, shell=True)


# CWE-284: Improper Access Control
# The vulnerable line is line 2, where user input is directly used to execute a shell command without proper validation. An attacker can use this to execute arbitrary commands on the system.