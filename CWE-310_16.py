#7.# CWE-310: Cryptographic Issues - Use of a One-Way Hash without a Salt
import hashlib
password = "password123"
hash = hashlib.sha256(password.encode()) # vulnerable line
print("Your hashed password is:", hash.hexdigest())