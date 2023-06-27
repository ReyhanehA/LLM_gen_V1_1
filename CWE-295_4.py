#5.# CWE-295: Improper Certificate Validation
# Vulnerable line: if not cert.has_expired():
import ssl
context = ssl.create_default_context()
with open("example.com.crt", "rb") as f:
    cert = ssl.PEM_cert_to_X509(f.read())
if not cert.has_expired():
    print("Certificate is still valid")