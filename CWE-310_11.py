#2.# CWE-310: Cryptographic Issues - Use of a Broken or Risky Cryptographic Algorithm
import hashlib
password = "password123"
hash = hashlib.md5(password.encode()) # vulnerable line
print("Your hashed password is:", hash.hexdigest())