#3.# CWE-321: Use of Hard-coded API Key
# Vulnerable line: api_key = "myapikey"
import requests
url = "https://example.com/api"
headers = {"Authorization": "Bearer " + api_key}
response = requests.get(url, headers=headers)