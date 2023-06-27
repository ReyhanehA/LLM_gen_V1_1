#10.# Example 10: CWE-310 - Cryptographic Issues

import hashlib

password = input("Enter your password: ")
hash_object = hashlib.sha512(password.encode())
if hash_object.hexdigest() == "cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e":
    print("Access granted") # CWE-310: Hardcoding password hashes in the code can lead to security vulnerabilities