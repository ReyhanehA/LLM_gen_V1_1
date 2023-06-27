#6.# Code with CWE-321:

import secrets

password = input("Enter your password: ")
key = secrets.token_bytes(16)

# Vulnerable line: key = secrets.token_bytes(16)
# Description: This code is vulnerable to CWE-321 (Use of Hard-coded Cryptographic Key) because it uses a hard-coded key instead of a secure cryptographic key.