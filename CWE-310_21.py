#2.# Example 2: CWE-310 - Cryptographic Issues

import base64

message = input("Enter your message: ")
encoded_message = base64.b64encode(message.encode())
print("Your encoded message is: " + encoded_message.decode()) # CWE-310: Base64 encoding is not a secure way to protect sensitive data