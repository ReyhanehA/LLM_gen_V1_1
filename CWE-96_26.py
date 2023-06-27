#8.# Example 8: Integer Overflow

import sys

x = sys.maxsize
y = int(input("Enter number: "))

# Vulnerable line: z = x + y
# Description: This code is vulnerable to integer overflow as it adds an arbitrary user input to a value that is already at the maximum limit of the integer data type.