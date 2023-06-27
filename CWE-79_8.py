#9.# CWE-79: OS Command Injection
# Vulnerable line:
os.system("rm " + filename)

# Description: This code is vulnerable to OS command injection as it concatenates user input directly into a system command without proper sanitization.