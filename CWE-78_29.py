#10.# Example 10:

import hashlib

password = input("Enter a password: ")
hashed_password = hashlib.sha256(password.encode()).hexdigest()

# CWE-78: Improper Neutralization of Special Elements used in a Hash Function
# Vulnerable line: hashlib.sha256(password.encode()).hexdigest()
# Description: The user input for password can be manipulated to generate a hash collision.