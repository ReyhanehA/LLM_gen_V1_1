#10.# Example 10: Use of os.popen() function with user-controlled input

import os

filename = input("Enter a filename: ")
os.popen("rm " + filename) # CWE-23: Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')