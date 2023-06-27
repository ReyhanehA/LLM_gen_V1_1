#7.# Example 7: Integer Overflow

import sys

x = sys.maxsize
y = x + 1

# Vulnerable line: y = x + 1
# Description: This code is vulnerable to integer overflow as it tries to store a value greater than the maximum value that can be stored in a variable.