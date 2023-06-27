#2.# Example 2: CWE-20 - Improper Input Validation

import os

filename = input("Enter a filename: ")
os.remove(filename)

# The vulnerable line is line 3, where the input is not validated and can potentially allow for deletion of unintended files.