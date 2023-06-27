#5.# Example 5: CWE-20 - Improper Input Validation

import subprocess

command = input("Enter a command: ")
subprocess.call(command)

# The vulnerable line is line 3, where the input is not validated and can potentially allow for executing unintended commands.