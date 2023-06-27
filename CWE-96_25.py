#7.# Example 7: Buffer Overflow

import ctypes

buffer = input("Enter buffer: ")

# Vulnerable line: ctypes.create_string_buffer(buffer)
# Description: This code is vulnerable to buffer overflow as it creates a buffer of arbitrary size without proper bounds checking.