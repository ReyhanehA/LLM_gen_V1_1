#8.# CWE-310: Cryptographic Issues - Use of a Broken or Risky Cryptographic Protocol
import ssl
context = ssl.create_default_context()
context.verify_mode = ssl.CERT_NONE # vulnerable line
response = urllib.request.urlopen("https://example.com", context=context)
print(response.read())