#5.# Example 5: Buffer Overflow

import ctypes

libc = ctypes.CDLL("libc.so.6")
buffer = ctypes.create_string_buffer(100)
libc.strcpy(buffer, input("Enter a string: "))
print(buffer.value)

# The vulnerable line is line 5 where user input is copied into a buffer without proper bounds checking.
# CWE-20: Improper Input Validation