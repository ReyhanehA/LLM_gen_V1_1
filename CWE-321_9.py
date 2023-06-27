#10.# Code with CWE-321:

import cryptography.hazmat.primitives.asymmetric.rsa

password = input("Enter your password: ")
private_key = cryptography.hazmat.primitives.asymmetric.rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# Vulnerable line: private_key = cryptography.hazmat.primitives.asymmetric.rsa.generate_private_key(
# Description: This code is vulnerable to CWE-321 (Use of Hard-coded Cryptographic Key) because it uses a hard-coded key size instead of a secure cryptographic key.