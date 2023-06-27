#7.# CWE-326: Insecure Storage of Sensitive Information
# Vulnerable line: key = "my_secret_key"
# Description: The secret key is hard-coded in the code, making it vulnerable to theft or unauthorized access.
import hmac

key = "my_secret_key"
message = input("Enter message: ")

hmac_object = hmac.new(key.encode(), message.encode(), hashlib.sha256)
print(hmac_object.hexdigest())