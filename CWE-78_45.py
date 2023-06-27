#6.# Example 6: Insecure Cryptographic Storage

import hashlib

password = input("Enter password: ")

hash = hashlib.md5(password.encode()).hexdigest()

# Vulnerable line: hash = hashlib.md5(password.encode()).hexdigest()
# Description: This code is vulnerable to insecure cryptographic storage as it uses a weak hashing algorithm (MD5) to store passwords.