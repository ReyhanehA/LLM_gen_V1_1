#5.# Example 5: Insecure Cryptographic Storage

import hashlib

password = input("Enter password: ")

# Vulnerable line: hashed_password = hashlib.md5(password.encode()).hexdigest()
# Description: This code is vulnerable to insecure cryptographic storage as it uses the weak MD5 hashing algorithm to store passwords.