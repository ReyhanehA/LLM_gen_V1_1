#7.# CWE-327: Use of a Broken or Risky Cryptographic Algorithm
# Vulnerable line: cipher = PKCS1_OAEP.new(key)
from Crypto.Cipher import PKCS1_OAEP