#7.# Example 7: Use of os.system() function with user-controlled input

import os

filename = input("Enter a filename: ")
os.system("rm " + filename) # CWE-23: Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')