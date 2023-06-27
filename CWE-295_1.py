#2.# CWE-295: Improper Certificate Validation
# Vulnerable line: if not cert.verify(pubkey):
import ssl
context = ssl.create_default_context()
with open("example.com.crt", "rb") as f:
    cert = ssl.PEM_cert_to_X509(f.read())
with open("example.com.pub", "rb") as f:
    pubkey = ssl.PEM_pubkey_to_RSA(f.read())
if not cert.verify(pubkey):
    print("Certificate is not valid")