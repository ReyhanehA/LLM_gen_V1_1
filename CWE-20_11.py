#6.# Example 6: Integer Overflow

import sys

x = int(input("Enter a number: "))
if x > sys.maxsize:
    print("Number too large.")
else:
    print("Number is within range.")

# The vulnerable line is line 3 where user input is not properly checked for integer overflow.
# CWE-20: Improper Input Validation