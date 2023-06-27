#10.# CWE-96: Improper Neutralization of Directives in Statically Saved Code (XSS)

import requests

url = input("Enter a URL: ")
response = requests.get(url)

print(response.text)

# The vulnerable line is line 2 where user input is directly used in a URL without proper sanitization, allowing for potential XSS attacks.