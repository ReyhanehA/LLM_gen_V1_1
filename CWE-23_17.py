#8.# Example 8: Use of subprocess.call() function with user-controlled input

import subprocess

filename = input("Enter a filename: ")
subprocess.call(["rm", filename]) # CWE-23: Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')