#1.# Example 1: CWE-321 - Use of Hard-coded Cryptographic Key
key = "mysecretkey"
cipher = AES.new(key, AES.MODE_CBC, iv)

# The hard-coded key "mysecretkey" is vulnerable to attacks as it can be easily guessed or extracted.