#6.# Example 6: Buffer Overflow

import ctypes

buffer = ctypes.create_string_buffer(10)
data = input("Enter data: ")

ctypes.memmove(buffer, data, len(data))

# Vulnerable line: ctypes.memmove(buffer, data, len(data))
# Description: This code is vulnerable to buffer overflow as it allows the user to input more data than the allocated buffer can hold.