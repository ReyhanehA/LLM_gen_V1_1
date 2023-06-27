#5.# CWE-327: Use of a Broken or Risky Cryptographic Algorithm
# Vulnerable line: cipher = DES3.new(key, DES3.MODE_ECB)
from Crypto.Cipher import DES3