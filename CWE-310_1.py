#2.# CWE-310: Cryptographic Issues - Use of a Broken or Risky Cryptographic Algorithm
import hashlib
password = "password123"
hash_object = hashlib.md5(password.encode()) # vulnerable line
hash = hash_object.hexdigest()
# This code uses the broken and insecure cryptographic algorithm MD5 to hash the password.