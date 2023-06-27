#9.# CWE-327: Use of a Broken or Risky Cryptographic Algorithm
# Vulnerable line: cipher = ChaCha20.new(key)
from Crypto.Cipher import ChaCha20