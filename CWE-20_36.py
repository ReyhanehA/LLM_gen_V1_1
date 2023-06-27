#1.# Example 1: Improper Input Validation

input_data = input("Enter your name: ")
print("Hello, " + input_data)

# The vulnerable line is line 1 where user input is not validated
# CWE-20: Improper Input Validation
# This code is vulnerable to input injection attacks as it does not validate user input