#7.# Example 7: Use of subprocess module without proper input validation

import subprocess

command = input("Enter a command: ")
subprocess.call(command) # CWE-326: Insecure use of subprocess module