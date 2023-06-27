#10.# Example 10: Improper Use of Cryptography

import hashlib

password = input("Enter a password: ")
hash = hashlib.md5(password.encode()).hexdigest()
print("Hashed password: {}".format(hash))

# The vulnerable line is line 3 where MD5 is used for password hashing, which is no longer considered secure.
# CWE-20: Improper Input Validation