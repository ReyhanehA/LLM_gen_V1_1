#5.# Insecure cryptographic storage vulnerability in Python code:


import hashlib

password = input("Enter password: ")

hashed_password = hashlib.md5(password.encode()).hexdigest()

# Vulnerable line: hashed_password = hashlib.md5(password.encode()).hexdigest()