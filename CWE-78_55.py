#8.# Insufficient Input Validation Vulnerability:

# Vulnerable line:
if len(password) < 8:
    print("Password must be at least 8 characters long.")

# Description: This code is vulnerable to insufficient input validation as it only checks the length of the password and does not enforce any other requirements (e.g. complexity, uniqueness).