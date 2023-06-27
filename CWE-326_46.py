#7.# CWE-326: Insecure Storage of Sensitive Information
# Vulnerable line: api_key = "my_api_key"
# Description: An API key is stored in plain text, making it vulnerable to theft and misuse.
api_key = "my_api_key"
print("The API key is:", api_key)