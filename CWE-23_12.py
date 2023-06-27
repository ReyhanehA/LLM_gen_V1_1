#3.# Example 3: Use of subprocess.call() function without proper input validation

import subprocess

filename = input("Enter a filename: ")
subprocess.call(["rm", filename]) # CWE-23: Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')