#6.# CWE-310: Cryptographic Issues - Use of Insufficiently Random Values in a Security Context
import random
token = str(random.randint(100000, 999999)) # vulnerable line
# This code generates a token using the insufficiently random function randint() which can be easily predicted by an attacker.