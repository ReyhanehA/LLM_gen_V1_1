#5.# CWE-310: Cryptographic Issues - Use of Hard-coded Cryptographic Key
import hashlib
password = "password123"
key = hashlib.sha256(b"mysecretkey").digest() # vulnerable line
hash_object = hashlib.sha256(password.encode() + key)
hash = hash_object.hexdigest()
# This code uses a hard-coded cryptographic key which can be easily discovered by an attacker.