#5.# CWE-321: Use of Hard-coded Salt
# Vulnerable line: salt = "mysalt"
import hashlib
password = "mypassword"
hash_object = hashlib.sha256(salt.encode() + password.encode())
hex_dig = hash_object.hexdigest()