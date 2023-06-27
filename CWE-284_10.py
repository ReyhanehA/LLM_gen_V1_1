#1.# Example 1:


password = input("Enter your password: ")
if password == "password":
    print("Access granted!")
else:
    print("Access denied.")


# CWE-284: Improper Access Control
# The vulnerable line is line 2, where the password is compared to a hardcoded value "password". This allows an attacker to easily guess the password and gain unauthorized access.