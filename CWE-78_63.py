#7.# Integer overflow vulnerability in Python code:


import sys

num = int(input("Enter a number: "))

if num > sys.maxsize:
    print("Number too large")
else:
    print("Number is within range")

# Vulnerable line: if num > sys.maxsize: