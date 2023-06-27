#1.# CWE-310: Cryptographic Issues - Insecure Randomness
import random
key = random.randint(0, 1000) # vulnerable line
# This code generates a random key using the insecure random function randint() which can be easily predicted by an attacker.