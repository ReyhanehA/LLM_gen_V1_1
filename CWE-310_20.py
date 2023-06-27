#1.# Example 1: CWE-310 - Cryptographic Issues

import hashlib

password = input("Enter your password: ")
hash_object = hashlib.md5(password.encode())
print("Your hashed password is: " + hash_object.hexdigest()) # CWE-310: The use of MD5 for password hashing is insecure