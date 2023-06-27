#4.# Example 4: CWE-284 - Improper Access Control

import urllib.request

url = "http://example.com/secret_file"
response = urllib.request.urlopen(url)
print(response.read())

# The vulnerable line is line 3 where the code reads a file from a remote server without checking if the user has permission to access it.