#10.# CWE-310: Cryptographic Issues - Use of Insufficiently Random Values in a Security Context
import os
key = os.urandom(16) # vulnerable line
print("Your encryption key is:", key)