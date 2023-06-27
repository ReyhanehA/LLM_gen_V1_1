#8.# CWE-321: Use of Hard-coded Username
# Vulnerable line: username = "myusername"
import requests
url = "https://example.com/login"
data = {"username": username, "password": "mypassword"}
response = requests.post(url, data=data)