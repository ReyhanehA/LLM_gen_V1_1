#5.# Example 5: CWE-321 - Use of Unvalidated Input
username = input("Enter your username: ")
password = input("Enter your password: ")
if username == "admin" and password == "password":
    print("Login successful")
else:
    print("Invalid username or password")

# The use of input() function is vulnerable to attacks as it allows users to input malicious code or characters.