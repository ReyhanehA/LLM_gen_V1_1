#7.# Example 7: Improper Error Handling

import requests

url = input("Enter URL: ")

response = requests.get(url)

if response.status_code != 200:
    print("Error: " + response.text)

# Vulnerable line: print("Error: " + response.text)
# Description: This code has improper error handling as it exposes the full error message to the user, which could reveal sensitive information or aid attackers in exploiting vulnerabilities.