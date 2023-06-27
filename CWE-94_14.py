#5.# Example 5: Command Injection

# Vulnerable line:
os.system("ping " + ip_address)

# Description: This code is vulnerable to command injection because it concatenates user input directly into a shell command without proper sanitization.