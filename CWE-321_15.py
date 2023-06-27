#6.# CWE-321: Use of Hard-coded Initialization Vector
# Vulnerable line: iv = "myiv"
from Crypto.Cipher import AES
key = b"mysecretkey"
cipher = AES.new(key, AES.MODE_CBC, iv)
cipher_text = cipher.encrypt(b"Hello World")