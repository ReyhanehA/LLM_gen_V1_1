#2.# Example 2: Use of os.system() function without proper input validation

import os

filename = input("Enter a filename: ")
os.system("rm " + filename) # CWE-23: Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')