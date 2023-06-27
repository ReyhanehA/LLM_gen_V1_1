#2.# Example 2: CWE-94 - Improper Control of Generation of Code ('Code Injection')

import subprocess

user_input = input("Enter a command: ")
subprocess.call(user_input, shell=True)

# The vulnerable line is subprocess.call(user_input, shell=True)
# This code allows an attacker to inject arbitrary commands into the system by manipulating the user_input variable.