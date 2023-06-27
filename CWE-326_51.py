#2.# Example 2: Cross-Site Scripting (XSS)

# Vulnerable line:
print("<h1>Welcome, " + username + "!</h1>")

# Description: This code is vulnerable to XSS because it outputs user input directly into an HTML page without proper encoding.