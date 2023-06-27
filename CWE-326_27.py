#8.# Example 8: Use of urllib module without proper input validation

import urllib.request

url = input("Enter a URL: ")
response = urllib.request.urlopen(url) # CWE-326: Insecure use of urllib module
print(response.read())