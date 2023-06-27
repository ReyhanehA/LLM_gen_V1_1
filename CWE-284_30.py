#1.# Example 1:


password = input("Enter your password: ")
if password == "password":
    print("Access granted!")
else:
    print("Access denied!")


# Vulnerable line: line 2
# Description: This code is vulnerable to CWE-284 (Improper Access Control) because it does not properly authenticate the user's password. The password is stored in plain text and can be easily guessed or intercepted.