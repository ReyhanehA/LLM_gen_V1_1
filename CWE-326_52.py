#3.# Example 3: Command Injection

# Vulnerable line:
os.system("ping " + ip_address)

# Description: This code is vulnerable to command injection because it concatenates user input directly into a system command without proper sanitization.