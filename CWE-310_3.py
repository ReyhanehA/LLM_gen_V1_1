#4.# CWE-310: Cryptographic Issues - Weak Encryption
from cryptography.fernet import Fernet
key = Fernet.generate_key() # vulnerable line
cipher_suite = Fernet(key)
message = "secret message".encode()
cipher_text = cipher_suite.encrypt(message)
# This code uses the weak encryption algorithm Fernet which can be easily cracked by an attacker.