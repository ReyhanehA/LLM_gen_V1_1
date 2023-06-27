#10.# CWE-327: Use of a Broken or Risky Cryptographic Algorithm
# Vulnerable line: cipher = Salsa20.new(key)
from Crypto.Cipher import Salsa20