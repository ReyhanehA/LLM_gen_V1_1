#3.# Example 3:


import requests

url = input("Enter a URL: ")
response = requests.get(url)
if response.status_code == 200:
    print(response.text)
else:
    print("Error:", response.status_code)


# CWE-284: Improper Access Control
# The vulnerable line is line 2, where the user input is used to construct a URL without proper validation. An attacker can use this to make arbitrary HTTP requests.