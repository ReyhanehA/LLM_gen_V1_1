#8.# Example 8: CWE-321 - Use of Unvalidated Input for Network Operations
host = input("Enter the hostname: ")
port = input("Enter the port number: ")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, int(port)))

# The use of unvalidated input for network operations is vulnerable to buffer overflow attacks.