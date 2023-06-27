#8.# CWE-96: Improper Neutralization of Directives in Statically Saved Code (XSS)

import os

filename = input("Enter a filename: ")
os.remove(filename)

# The vulnerable line is line 2 where user input is directly used in a file operation without proper sanitization, allowing for potential directory traversal attacks.