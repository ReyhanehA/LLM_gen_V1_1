#10.# Code with CWE-78: Expression Injection via eval()

expression = input("Enter expression: ")
result = eval("2 + " + expression)

# Vulnerable line: result = eval("2 + " + expression)
# Description: This code is vulnerable to expression injection via eval() as it concatenates user input directly into the expression without proper validation or sanitization.