#10.# CWE-326: Insecure Storage of Sensitive Information
# Vulnerable line: print(key)
# Description: The secret key used for encryption is printed to the console in plain text, making it vulnerable to theft or unauthorized access.
import hashlib

key = "my_secret_key"
message = "sensitive information"
hash_object = hashlib.sha256(key.encode() + message.encode())
hex_dig = hash_object.hexdigest()
print(key)