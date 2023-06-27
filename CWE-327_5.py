#6.# CWE-327: Use of a Broken or Risky Cryptographic Algorithm
# Vulnerable line: cipher = XOR.new(key)
from Crypto.Cipher import XOR