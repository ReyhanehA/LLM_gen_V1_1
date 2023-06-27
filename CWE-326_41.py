#2.# CWE-326: Insecure Storage of Sensitive Information
# Vulnerable line: f.write(data)
# Description: Sensitive data is written to a file without any encryption or protection, making it vulnerable to theft.
data = "This is sensitive information"
with open("data.txt", "w") as f:
    f.write(data)