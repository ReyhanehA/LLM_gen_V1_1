#7.# CWE-310: Cryptographic Issues - Use of a One-Way Hash without a Salt
import hashlib
password = "password123"
hash_object = hashlib.sha256(password.encode()) # vulnerable line
hash = hash_object.hexdigest()
# This code uses a one-way hash without a salt which can make it easier for an attacker to crack the hash.