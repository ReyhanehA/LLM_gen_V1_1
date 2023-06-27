#5.# Example 5: CWE-310 - Cryptographic Issues

import hashlib

message = input("Enter your message: ")
hash_object = hashlib.sha1(message.encode())
print("Your hashed message is: " + hash_object.hexdigest()) # CWE-310: SHA-1 is no longer considered a secure hashing algorithm