#9.# Example 9: Path Traversal

import os

filename = input("Enter filename: ")

# Vulnerable line: with open(os.path.join('/var/www/html', filename), 'r') as f:
# Description: This code is vulnerable to path traversal as it allows a user to access files outside of the intended directory by manipulating the filename input.