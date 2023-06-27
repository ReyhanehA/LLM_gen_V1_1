#9.# Code with CWE-78: Code Injection via eval()

code = input("Enter code: ")
result = eval(code)

# Vulnerable line: result = eval(code)
# Description: This code is vulnerable to code injection via eval() as it executes user input as code without proper validation or sanitization.