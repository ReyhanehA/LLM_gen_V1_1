#3.# CWE-94: Improper Control of Generation of Code ('Code Injection')
# Vulnerable line: subprocess.call(user_input)
import subprocess
user_input = input("Enter a command to execute: ")
subprocess.call(user_input)