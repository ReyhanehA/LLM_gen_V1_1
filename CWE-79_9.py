#10.# CWE-79: Server-Side Request Forgery (SSRF)
# Vulnerable line:
response = requests.get(url)

# Description: This code is vulnerable to SSRF as it sends a request to a URL specified by user input without proper validation.