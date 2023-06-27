#6.# Code with CWE-78: Code Injection

import sys

code = input("Enter code: ")
exec(code)

# Vulnerable line: exec(code)
# Description: This code is vulnerable to code injection as it executes user input as code without proper validation or sanitization.