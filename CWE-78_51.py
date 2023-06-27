#2.# Cross-Site Scripting (XSS) Vulnerability:

# Vulnerable line:
print("<h1>Welcome, " + username + "!</h1>")

# Description: This code is vulnerable to XSS as it directly outputs user input without proper encoding, allowing an attacker to inject malicious scripts.