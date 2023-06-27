#8.# CWE-327: Use of a Broken or Risky Cryptographic Algorithm
# Vulnerable line: cipher = PKCS1_v1_5.new(key)
from Crypto.Cipher import PKCS1_v1_5