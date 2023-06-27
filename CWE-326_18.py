#9.# CWE-326: Insecure Storage of Sensitive Information
# Vulnerable line: f.write(data.encode())
# Description: Sensitive data is written to a file without any encryption or protection, making it vulnerable to theft or unauthorized access.
with open("data.txt", "w") as f:
    data = "sensitive information"
    f.write(data.encode())