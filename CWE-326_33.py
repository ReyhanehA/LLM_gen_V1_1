#4.# CWE-326: Insecure Storage of Sensitive Information
# Vulnerable line: key = "my_secret_key"
# Description: The secret key is hard-coded in the code, making it vulnerable to theft or unauthorized access.
import hashlib

key = "my_secret_key"
password = input("Enter password: ")

hash_object = hashlib.sha256(key.encode() + password.encode())
print(hash_object.hexdigest())