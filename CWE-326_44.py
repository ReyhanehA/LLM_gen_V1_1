#5.# CWE-326: Insecure Storage of Sensitive Information
# Vulnerable line: token = "my_access_token"
# Description: An access token is stored in plain text, making it vulnerable to theft and misuse.
token = "my_access_token"
print("The access token is:", token)