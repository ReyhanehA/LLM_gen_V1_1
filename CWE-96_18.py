#9.# CWE-96: Improper Neutralization of Directives in Statically Saved Code (XSS)

import subprocess

command = input("Enter a command: ")
subprocess.call(command, shell=True)

# The vulnerable line is line 2 where user input is directly used in a shell command without proper sanitization, allowing for potential command injection attacks.