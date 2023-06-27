#1.# Example 1: CWE-20 - Improper Input Validation

input_data = input("Enter your name: ")
print("Hello, " + input_data + "!")

# The vulnerable line is line 2, where the input is not validated and can potentially allow for malicious input.