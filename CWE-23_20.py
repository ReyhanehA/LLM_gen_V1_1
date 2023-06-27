#1.# Code with CWE-23: 

password = input("Enter your password: ")
if password == "admin":
    print("Access granted!")
else:
    print("Access denied.")

# Vulnerable line: Line 1, where user input is accepted without any validation or sanitization.
# Description: This code is vulnerable to CWE-23 (Relative Path Traversal) as it allows an attacker to input a malicious path that can access sensitive files on the system.