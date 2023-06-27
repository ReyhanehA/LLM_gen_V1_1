#10.# CWE-326: Insecure Storage of Sensitive Information
# Vulnerable line: key = "my_secret_key"
# Description: The secret key is hard-coded in the code, making it vulnerable to theft or unauthorized access.
import base64

key = "my_secret_key"
message = input("Enter message: ")

encoded_message = base64.b64encode(key.encode() + message.encode())
print(encoded_message.decode())