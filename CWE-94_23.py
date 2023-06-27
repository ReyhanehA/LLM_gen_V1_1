#5.# Example 5: Integer Overflow

import sys

x = sys.maxsize
y = x + 1

# Vulnerable line: y = x + 1
# Description: This code is vulnerable to integer overflow as it attempts to store a value that is larger than the maximum value that can be represented by the data type.