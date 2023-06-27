#3.# CWE-295: Improper Certificate Validation
# Vulnerable line: if not cert.verify(pubkey):
# Description: This code does not properly validate the certificate, allowing for potential man-in-the-middle attacks.
import ssl

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

with open('cert.pem', 'rb') as f:
    cert = ssl.PEM_cert_to_DER_cert(f.read())
    pubkey = ssl.DER_cert_to_PEM_cert(cert).public_key()

if not cert.verify(pubkey):
    print("Certificate validation failed.")