#3.# Example 3: CWE-321 - Use of Insufficiently Random Values
nonce = 12345
cipher = AES.new(key, AES.MODE_CBC, nonce)

# The use of a non-random nonce value is vulnerable to attacks as it can be predicted and exploited.