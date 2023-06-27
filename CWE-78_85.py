#9.# Insecure Cryptographic Storage:


import hashlib

password = input("Enter password: ")

with open('password.txt', 'w') as f:
    f.write(hashlib.md5(password.encode()).hexdigest())

# The vulnerable line is the use of MD5 for password hashing, which is insecure and susceptible to attacks.