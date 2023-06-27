#6.# CWE-326: Insecure Storage of Sensitive Information
# Vulnerable line: f.write(password)
# Description: The user's password is written to a file in plain text, making it vulnerable to theft or unauthorized access.
with open("password.txt", "w") as f:
    password = input("Enter your password: ")
    f.write(password)