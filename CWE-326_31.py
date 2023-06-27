#2.# CWE-326: Insecure Storage of Sensitive Information
# Vulnerable line: f.write(data)
# Description: The data is written to a file without any encryption or protection, making it vulnerable to theft or unauthorized access.
with open("file.txt", "w") as f:
    data = input("Enter sensitive information: ")
    f.write(data)