#7.# Example 7: Insecure Cryptographic Storage

# Vulnerable line:
hashed_password = hashlib.md5(password.encode()).hexdigest()

# Description: This code is vulnerable to insecure cryptographic storage because it uses a weak hashing algorithm that can be easily cracked.