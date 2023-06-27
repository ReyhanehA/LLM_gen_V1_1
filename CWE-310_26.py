#7.# Example 7: CWE-310 - Cryptographic Issues

import hashlib

password = input("Enter your password: ")
hash_object = hashlib.md5(password.encode())
if hash_object.hexdigest() == "5f4dcc3b5aa765d61d8327deb882cf99":
    print("Access granted") # CWE-310: Hardcoding password hashes in the code can lead to security vulnerabilities