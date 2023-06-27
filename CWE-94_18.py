#9.# Example 9: Improper Error Handling

# Vulnerable line:
try:
    result = 1 / 0
except:
    print("An error occurred.")

# Description: This code is vulnerable to improper error handling because it catches all exceptions without providing any useful information about the error.