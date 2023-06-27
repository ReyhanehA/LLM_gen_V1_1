#4.# CWE-310: Cryptographic Issues - Weak Encryption
from cryptography.fernet import Fernet
key = Fernet.generate_key() # vulnerable line
cipher_suite = Fernet(key)
message = "This is a secret message"
cipher_text = cipher_suite.encrypt(message.encode())
print("Your encrypted message is:", cipher_text)