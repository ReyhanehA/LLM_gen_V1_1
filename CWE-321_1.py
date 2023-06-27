#2.# Code with CWE-321:

import hashlib

password = input("Enter your password: ")
hash_object = hashlib.sha256(b'password')
hex_dig = hash_object.hexdigest()

# Vulnerable line: hash_object = hashlib.sha256(b'password')
# Description: This code is vulnerable to CWE-321 (Use of Hard-coded Cryptographic Key) because it uses a hard-coded password instead of a secure cryptographic key.