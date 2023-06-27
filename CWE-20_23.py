#8.# Example 8: Integer Overflow

import sys

x = int(sys.argv[1])
y = int(sys.argv[2])

result = x * y

if result < 0:
    print("Error: Integer overflow")

# Vulnerable line: result = x * y
# Description: This code is vulnerable to integer overflow as it does not check if the result of the multiplication exceeds the maximum value that can be stored in an integer.