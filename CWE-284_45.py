#6.# Example 6: Improper Error Handling

import requests

url = input("Enter URL: ")
response = requests.get(url)

if response.status_code != 200:
    # Vulnerable line: print("Error: " + response.text)
    # Description: This code has improper error handling as it exposes sensitive information (response text) to the user in case of an error.
    print("Error: " + response.text)