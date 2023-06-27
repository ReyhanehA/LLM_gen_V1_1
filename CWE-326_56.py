#8.# Example 8: Improper Error Handling

# Vulnerable line:
try:
    result = divide(num1, num2)
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Description: This code is vulnerable to improper error handling because it does not provide enough information about the error that occurred, which could lead to security vulnerabilities.