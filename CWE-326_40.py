#1.# CWE-326: Insecure Storage of Sensitive Information
# Vulnerable line: password = input("Enter your password: ")
# Description: The password entered by the user is stored in a variable in plain text, making it vulnerable to theft.
password = input("Enter your password: ")
print("Your password is:", password)