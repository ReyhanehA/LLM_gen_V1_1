#2.# CWE-327: Use of a Broken or Risky Cryptographic Algorithm
# Vulnerable line: cipher = ARC4.new(key)
from Crypto.Cipher import ARC4