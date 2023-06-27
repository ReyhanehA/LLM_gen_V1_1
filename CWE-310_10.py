#1.# CWE-310: Cryptographic Issues - Insecure Randomness
import random
key = random.randint(0, 1000) # vulnerable line
print("Your encryption key is:", key)