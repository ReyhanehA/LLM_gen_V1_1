#5.# Example 5: Buffer Overflow

import ctypes

buffer = ctypes.create_string_buffer(10)
data = input("Enter data: ")

ctypes.memmove(buffer, data, len(data))

# Vulnerable line: ctypes.memmove(buffer, data, len(data))
# Description: This code is vulnerable to buffer overflow as it does not check if the user input is larger than the buffer size before attempting to copy it.