#8.# Example 8: CWE-310 - Cryptographic Issues

import hashlib

password = input("Enter your password: ")
hash_object = hashlib.sha1(password.encode())
if hash_object.hexdigest() == "a94a8fe5ccb19ba61c4c0873d391e987982fbbd3":
    print("Access granted") # CWE-310: Hardcoding password hashes in the code can lead to security vulnerabilities