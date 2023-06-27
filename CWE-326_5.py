#6.# CWE-326: Insecure Storage of Sensitive Information
# Vulnerable line: f = open("config.txt", "r")
# Description: The configuration file is opened without any encryption or protection, making it vulnerable to theft or unauthorized access.

f = open("config.txt", "r")
data = f.read()
f.close()