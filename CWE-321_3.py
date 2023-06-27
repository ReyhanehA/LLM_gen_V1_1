#4.# Code with CWE-321:

import hmac

password = input("Enter your password: ")
key = b'secret_key'
h = hmac.new(key, password.encode('utf-8'), hashlib.sha256)

# Vulnerable line: key = b'secret_key'
# Description: This code is vulnerable to CWE-321 (Use of Hard-coded Cryptographic Key) because it uses a hard-coded key instead of a secure cryptographic key.