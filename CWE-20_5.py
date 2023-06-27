#10.# Example 10: Format String Vulnerability

name = input("Enter your name: ")
print("Hello, %s!" % name)

# The vulnerable line is line 2 where user input is used in a format string
# CWE-20: Improper Input Validation
# This code is vulnerable to format string attacks as it does not properly sanitize user input