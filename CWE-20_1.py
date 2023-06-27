#6.# Example 6: Integer Overflow

import sys

a = sys.maxsize
b = 2

c = a + b
print(c)

# The vulnerable line is line 5 where an integer overflow can occur
# CWE-20: Improper Input Validation
# This code is vulnerable to integer overflow attacks as it does not properly check the size of the integers