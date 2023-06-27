#1.# CWE-321: Use of Hard-coded Cryptographic Key
# Vulnerable line: key = "mysecretkey"
import hashlib
message = "Hello World"
hash_object = hashlib.sha256(key.encode() + message.encode())
hex_dig = hash_object.hexdigest()