#9.# Insecure Cryptographic Storage:


import hashlib

password = input("Enter password: ")
hash = hashlib.md5(password.encode()).hexdigest()

# The vulnerable line is the use of MD5 for password hashing, which is insecure and can be easily cracked.