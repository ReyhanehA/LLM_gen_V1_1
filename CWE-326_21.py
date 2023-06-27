#2.# Example 2: Use of os.system() function without proper input validation

import os

filename = input("Enter a filename: ")
os.system("rm " + filename) # CWE-326: Insecure use of os.system() function