#4.# Example 4: CWE-310 - Cryptographic Issues

import hashlib

password = input("Enter your password: ")
salt = "random_salt"
hash_object = hashlib.sha256((password + salt).encode())
print("Your hashed password is: " + hash_object.hexdigest()) # CWE-310: Using a static salt for password hashing can lead to security vulnerabilities