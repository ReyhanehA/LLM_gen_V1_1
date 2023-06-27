#1.# CWE-327: Use of a Broken or Risky Cryptographic Algorithm
# Vulnerable line: cipher = DES.new(key, DES.MODE_ECB)
# Description: Using the DES algorithm in Electronic Codebook (ECB) mode is insecure and can lead to predictable ciphertext.
from Crypto.Cipher import DES

key = b'secretkey'
plaintext = b'my secret message'

cipher = DES.new(key, DES.MODE_ECB)
ciphertext = cipher.encrypt(plaintext)