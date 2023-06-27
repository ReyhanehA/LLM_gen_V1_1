#8.# CWE-310: Cryptographic Issues - Use of a Predictable Algorithm in a Security Context
import hashlib
password = "password123"
hash_object = hashlib.sha1(password.encode()) # vulnerable line
hash = hash_object.hexdigest()
# This code uses the predictable algorithm SHA1 which can be easily cracked by an attacker.