#9.# Example 9: CWE-310 - Cryptographic Issues

import hashlib

password = input("Enter your password: ")
hash_object = hashlib.sha256(password.encode())
if hash_object.hexdigest() == "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8":
    print("Access granted") # CWE-310: Hardcoding password hashes in the code can lead to security vulnerabilities