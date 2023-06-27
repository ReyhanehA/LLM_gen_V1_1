#8.# Integer Overflow:


import sys

x = int(sys.argv[1])
y = int(sys.argv[2])

if x + y < x:
    print("Integer overflow!")
else:
    print(x + y)

# The vulnerable line is the lack of proper integer overflow checking, allowing for integer overflow attacks.