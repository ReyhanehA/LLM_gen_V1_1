#8.# Example 8: CWE-20 - Improper Input Validation

import socket

host = input("Enter a host: ")
port = input("Enter a port: ")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# The vulnerable line is line 4, where the input is not validated and can potentially allow for connecting to unintended hosts and ports.