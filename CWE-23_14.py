#5.# Example 5: Use of os.popen() function without proper input validation

import os

filename = input("Enter a filename: ")
os.popen("rm " + filename) # CWE-23: Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')