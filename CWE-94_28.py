#10.# Example 10: Improper Error Handling

import requests

url = input("Enter URL: ")

response = requests.get(url)

if response.status_code != 200:
    print("Error: " + response.text)

# Vulnerable line: print("Error: " + response.text)
# Description: This code is vulnerable to improper error handling as it exposes sensitive information to the user in the error message.