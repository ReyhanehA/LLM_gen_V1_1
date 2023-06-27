#8.# Integer Overflow:


import sys

x = int(sys.argv[1])
if x > 2147483647:
    print("Integer overflow!")
else:
    print("No integer overflow.")


# The vulnerable line is line 3, where an integer overflow can occur if the input value is greater than the maximum value of a 32-bit signed integer.