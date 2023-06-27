#3.# Example 3: CWE-310 - Cryptographic Issues

import hmac

message = input("Enter your message: ")
key = input("Enter your key: ")
hmac_object = hmac.new(key.encode(), message.encode())
print("Your HMAC is: " + hmac_object.hexdigest()) # CWE-310: Using a weak key for HMAC can lead to security vulnerabilities