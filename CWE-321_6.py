#7.# Code with CWE-321:

import cryptography.fernet

password = input("Enter your password: ")
key = cryptography.fernet.Fernet.generate_key()

# Vulnerable line: key = cryptography.fernet.Fernet.generate_key()
# Description: This code is vulnerable to CWE-321 (Use of Hard-coded Cryptographic Key) because it uses a hard-coded key instead of a secure cryptographic key.