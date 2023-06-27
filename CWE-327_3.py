#4.# CWE-327: Use of a Broken or Risky Cryptographic Algorithm
# Vulnerable line: cipher = AES.new(key, AES.MODE_ECB)
from Crypto.Cipher import AES