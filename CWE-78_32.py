#3.# Example 3:


import subprocess

command = input("Enter a command: ")
subprocess.call(command, shell=True)


# CWE-78: Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')
# Vulnerable line: subprocess.call(command, shell=True)
# Description: The user input is passed directly to the shell, allowing for arbitrary command execution.