#4.# Example 4: Command Injection

import subprocess

command = input("Enter command: ")
subprocess.call(command)

# Vulnerable line: subprocess.call(command)
# Description: This code is vulnerable to command injection as it executes user input directly as a command without proper sanitization.