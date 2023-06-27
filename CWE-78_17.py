#8.# Example 8: Code Injection

import sys

code = input("Enter code: ")

# CWE-78: The user input is not properly sanitized and can be used to inject code
# Vulnerable line: exec(code)
exec("print('Hello, world!')")