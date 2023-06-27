#6.# Example 6: CWE-321 - Use of Unvalidated Input
username = input("Enter your username: ")
password = input("Enter your password: ")
if username == "admin" and password == "password":
    print("Access granted")
else:
    print("Access denied")

# The use of unvalidated input for username and password is vulnerable to attacks as it can be easily manipulated and exploited.