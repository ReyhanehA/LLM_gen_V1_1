#9.# Example 9: Integer Overflow

import sys

num = int(input("Enter number: "))

if num > sys.maxsize:
    print("Number is too large!")

# Vulnerable line: if num > sys.maxsize:
# Description: This code is vulnerable to integer overflow as it does not properly handle numbers that exceed the maximum value for the system.