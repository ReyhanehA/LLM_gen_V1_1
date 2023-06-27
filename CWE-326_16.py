#7.# CWE-326: Insecure Storage of Sensitive Information
# Vulnerable line: print(data)
# Description: Sensitive data is printed to the console in plain text, making it vulnerable to theft or unauthorized access.
data = "sensitive information"
print(data)