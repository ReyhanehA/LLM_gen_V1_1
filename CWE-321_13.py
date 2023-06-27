#4.# CWE-321: Use of Hard-coded Encryption Algorithm
# Vulnerable line: cipher = "AES-256-CBC"
from cryptography.fernet import Fernet
key = Fernet.generate_key()
cipher_suite = Fernet(key)
cipher_text = cipher_suite.encrypt(b"Hello World")