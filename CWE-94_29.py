#1.# Example 1: CWE-94 - Improper Control of Generation of Code ('Code Injection')

import os

user_input = input("Enter a file name: ")
os.system("cat " + user_input)

# The vulnerable line is os.system("cat " + user_input)
# This code allows an attacker to inject arbitrary commands into the system by manipulating the user_input variable.