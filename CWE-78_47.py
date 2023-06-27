#8.# Example 8: Buffer Overflow

import ctypes

buffer = ctypes.create_string_buffer(10)
input_str = input("Enter string: ")

ctypes.memmove(buffer, input_str, len(input_str))

# Vulnerable line: ctypes.memmove(buffer, input_str, len(input_str))
# Description: This code is vulnerable to buffer overflow as it allows a user to input a string that is longer than the allocated buffer size.