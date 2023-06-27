#3.# CWE-327: Use of a Broken or Risky Cryptographic Algorithm
# Vulnerable line: cipher = Blowfish.new(key)
from Crypto.Cipher import Blowfish