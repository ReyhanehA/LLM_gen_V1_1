#9.# CWE-326: Insecure Storage of Sensitive Information
# Vulnerable line: f = open("log.txt", "a")
# Description: The log file is opened without any encryption or protection, making it vulnerable to theft or unauthorized access.

f = open("log.txt", "a")
f.write("log message")
f.close()