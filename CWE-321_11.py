#2.# CWE-321: Use of Hard-coded Password
# Vulnerable line: password = "mypassword"
import requests
url = "https://example.com/login"
data = {"username": "myusername", "password": password}
response = requests.post(url, data=data)