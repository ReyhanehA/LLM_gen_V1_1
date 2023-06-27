#3.# Command Injection Vulnerability:

# Vulnerable line:
os.system("ping " + ip_address)

# Description: This code is vulnerable to command injection as it concatenates user input directly into a system command without proper sanitization, allowing an attacker to execute arbitrary commands.