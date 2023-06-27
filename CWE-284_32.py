#3.# Example 3:


import requests

url = input("Enter a URL: ")
response = requests.get(url)
if response.status_code == 200:
    print(response.text)
else:
    print("Error:", response.status_code)


# Vulnerable line: line 2
# Description: This code is vulnerable to CWE-284 (Improper Access Control) because it does not properly validate the user's input. An attacker could enter a malicious URL and potentially access sensitive information or execute arbitrary code on the system.