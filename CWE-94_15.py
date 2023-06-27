#6.# Example 6: Integer Overflow

# Vulnerable line:
result = 1
for i in range(1, n+1):
    result *= i

# Description: This code is vulnerable to integer overflow because it does not check if the result variable exceeds the maximum value for the data type.