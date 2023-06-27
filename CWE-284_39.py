#10.# Example 10:


import hashlib

password = input("Enter your password: ")
hashlib.md5(password.encode()).hexdigest()


# Vulnerable line: line 2
# Description: This code is vulnerable to CWE-284 (Improper Access Control) because it does not properly store the user's password. MD5 is a weak hashing algorithm and can be easily cracked, allowing an attacker to access the user's password.