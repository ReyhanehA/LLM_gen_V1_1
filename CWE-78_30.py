#1.# Example 1:


password = input("Enter your password: ")
if password == "password123":
    print("Access granted!")
else:
    print("Access denied.")


# CWE-78: Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')
# Vulnerable line: password = input("Enter your password: ")
# Description: The input function allows for arbitrary user input, which can be used to inject malicious commands into the system.