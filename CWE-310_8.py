#9.# CWE-310: Cryptographic Issues - Use of a Cryptographically Weak Pseudo-Random Number Generator (PRNG)
import random
key = random.getrandbits(128) # vulnerable line
# This code uses the weak PRNG function getrandbits() which can result in weak keys.