#6.# CWE-310: Cryptographic Issues - Use of a Predictable Algorithm in a Security-Sensitive Context
import hmac
key = b'secret_key'
message = b'This is a secret message'
hash = hmac.new(key, message) # vulnerable line
print("Your HMAC hash is:", hash.hexdigest())