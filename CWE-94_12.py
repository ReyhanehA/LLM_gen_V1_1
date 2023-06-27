#3.# Example 3: Buffer Overflow

# Vulnerable line:
buffer = bytearray(256)
input_data = input("Enter some data: ")
buffer[:len(input_data)] = input_data.encode()

# Description: This code is vulnerable to buffer overflow because it does not check the length of the user input before writing it to a fixed-size buffer.