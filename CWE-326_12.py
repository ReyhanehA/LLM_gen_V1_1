#3.# CWE-326: Insecure Storage of Sensitive Information
# Vulnerable line: print(password)
# Description: The password entered by the user is printed to the console in plain text, making it vulnerable to theft or unauthorized access.
password = input("Enter your password: ")
print(password)