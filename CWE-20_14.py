#9.# Example 9: Improper Error Handling

import requests

url = input("Enter a URL: ")
try:
    response = requests.get(url)
    response.raise_for_status()
    print(response.text)
except requests.exceptions.HTTPError as e:
    print("Error: {}".format(e))

# The vulnerable line is line 6 where the HTTP response status code is not properly checked for errors.
# CWE-20: Improper Input Validation