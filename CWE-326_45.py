#6.# CWE-326: Insecure Storage of Sensitive Information
# Vulnerable line: password = "my_password"
# Description: A password is stored in plain text, making it vulnerable to theft and misuse.
password = "my_password"
print("The password is:", password)