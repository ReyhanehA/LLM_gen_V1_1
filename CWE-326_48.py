#9.# CWE-326: Insecure Storage of Sensitive Information
# Vulnerable line: secret = "my_secret"
# Description: A secret value is stored in plain text, making it vulnerable to theft and misuse.
secret = "my_secret"
print("The secret value is:", secret)