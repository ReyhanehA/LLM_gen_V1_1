#7.# CWE-321: Use of Hard-coded Session ID
# Vulnerable line: session_id = "mysessionid"
import requests
url = "https://example.com/dashboard"
cookies = {"session_id": session_id}
response = requests.get(url, cookies=cookies)