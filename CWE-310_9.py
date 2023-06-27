#10.# CWE-310: Cryptographic Issues - Use of a Cryptographically Weak Hash Function
import hashlib
password = "password123"
hash_object = hashlib.md4(password.encode()) # vulnerable line
hash = hash_object.hexdigest()
# This code uses the weak hash function MD4 which can be easily cracked by an attacker.