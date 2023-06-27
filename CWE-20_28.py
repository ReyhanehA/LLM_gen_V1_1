#3.# Example 3: CWE-20 - Improper Input Validation

import urllib.request

url = input("Enter a URL: ")
response = urllib.request.urlopen(url)
print(response.read())

# The vulnerable line is line 3, where the input is not validated and can potentially allow for accessing unintended URLs.