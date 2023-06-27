#6.# Example 6: Insecure Cryptography

import hashlib

password = input("Enter password: ")

hash = hashlib.md5(password.encode()).hexdigest()

# Vulnerable line: hash = hashlib.md5(password.encode()).hexdigest()
# Description: This code is vulnerable to insecure cryptography as it uses the MD5 hashing algorithm, which is no longer considered secure.