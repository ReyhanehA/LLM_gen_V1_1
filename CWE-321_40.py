#1.# Code with CWE-321: 

password = input("Enter your password: ")
if password == "admin":
    print("Access granted!")
else:
    print("Access denied.")

# Vulnerable line: password = input("Enter your password: ")
# Description: This code is vulnerable to CWE-321 (Use of Hard-coded Cryptographic Key) because it uses a hard-coded password instead of a secure cryptographic key.