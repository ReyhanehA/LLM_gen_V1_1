#5.# Insecure Cryptographic Storage Vulnerability:

# Vulnerable line:
hashed_password = md5(password.encode()).hexdigest()

# Description: This code is vulnerable to insecure cryptographic storage as it uses a weak hashing algorithm (MD5) to store passwords, making it easy for an attacker to crack the hashes.