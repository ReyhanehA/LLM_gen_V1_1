#4.# Example 4: Command Injection

import subprocess

command = input("Enter command: ")

# Vulnerable line: output = subprocess.check_output(command, shell=True)
# Description: This code is vulnerable to command injection as it executes user input directly as a shell command without proper sanitization.