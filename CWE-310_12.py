#3.# CWE-310: Cryptographic Issues - Insufficient Entropy
import secrets
password = secrets.token_hex(16) # vulnerable line
print("Your secure password is:", password)