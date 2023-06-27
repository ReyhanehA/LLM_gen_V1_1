#9.# Example 9:

import base64

data = input("Enter some data: ")
encoded_data = base64.b64encode(data)

# CWE-78: Improper Neutralization of Special Elements used in a Base64 String
# Vulnerable line: base64.b64encode(data)
# Description: The user input for data can be manipulated to inject malicious code in the encoded string.