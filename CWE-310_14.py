#5.# CWE-310: Cryptographic Issues - Use of Hard-coded Cryptographic Key
import base64
key = base64.b64decode("aGVsbG8gd29ybGQ=") # vulnerable line
cipher_text = base64.b64decode("c29tZSBzdHJpbmc=")
print("Your decrypted message is:", cipher_text)