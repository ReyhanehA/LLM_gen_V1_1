#5.# Code with CWE-321:

import os

password = input("Enter your password: ")
salt = os.urandom(16)
key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

# Vulnerable line: salt = os.urandom(16)
# Description: This code is vulnerable to CWE-321 (Use of Hard-coded Cryptographic Key) because it uses a hard-coded salt instead of a secure cryptographic key.