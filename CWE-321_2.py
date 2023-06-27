#3.# Code with CWE-321:

import base64

password = input("Enter your password: ")
encoded = base64.b64encode(password.encode('utf-8'))

# Vulnerable line: encoded = base64.b64encode(password.encode('utf-8'))
# Description: This code is vulnerable to CWE-321 (Use of Hard-coded Cryptographic Key) because it uses a hard-coded password instead of a secure cryptographic key.