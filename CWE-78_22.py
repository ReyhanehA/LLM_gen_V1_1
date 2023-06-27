#3.# Example 3:

import subprocess

command = input("Enter a command: ")
subprocess.call(command)

# CWE-78: Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')
# Vulnerable line: subprocess.call(command)
# Description: The user input for command can be manipulated to execute arbitrary commands.