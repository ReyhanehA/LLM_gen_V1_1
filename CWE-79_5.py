#6.# CWE-79: Header Injection
# Vulnerable line:
response.headers["Location"] = redirect_url

# Description: This code is vulnerable to header injection as it concatenates user input directly into an HTTP header without proper validation.