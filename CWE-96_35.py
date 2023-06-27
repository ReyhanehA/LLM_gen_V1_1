#8.# Integer Overflow:


import sys

x = int(input("Enter number: "))
if x > sys.maxsize:
    print("Integer overflow")

# The vulnerable line is the comparison where user input is not properly validated, allowing for integer overflow attacks.