#4.# CWE-326: Insecure Storage of Sensitive Information
# Vulnerable line: key = "my_secret_key"
# Description: A secret key is stored in plain text, making it vulnerable to theft and misuse.
key = "my_secret_key"
print("The secret key is:", key)