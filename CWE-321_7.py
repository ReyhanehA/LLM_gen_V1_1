#8.# Code with CWE-321:

import nacl.secret

password = input("Enter your password: ")
key = nacl.secret.SecretBox.generate_key()

# Vulnerable line: key = nacl.secret.SecretBox.generate_key()
# Description: This code is vulnerable to CWE-321 (Use of Hard-coded Cryptographic Key) because it uses a hard-coded key instead of a secure cryptographic key.