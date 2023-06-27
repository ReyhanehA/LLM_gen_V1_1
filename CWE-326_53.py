#5.# Example 5: Insecure Cryptographic Storage

# Vulnerable line:
hashed_password = md5(password)

# Description: This code is vulnerable to insecure cryptographic storage because it uses a weak hashing algorithm that can be easily cracked.