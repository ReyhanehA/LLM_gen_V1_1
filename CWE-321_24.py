#5.# Example 5: CWE-321 - Use of Weak Password Storage
password = "mypassword"
hashed_password = hashlib.md5(password.encode()).hexdigest()

# The use of MD5 hashing algorithm for password storage is vulnerable to attacks as it is known to have weaknesses and can be easily cracked.