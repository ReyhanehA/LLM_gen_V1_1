#4.# CWE-96: Improper Neutralization of Directives in Statically Saved Code (XSS)

import urllib.parse

url = input("Enter a URL: ")
parsed_url = urllib.parse.urlparse(url)

print("Scheme: " + parsed_url.scheme)
print("Netloc: " + parsed_url.netloc)

# The vulnerable line is line 2 where user input is directly used in a URL without proper sanitization, allowing for potential XSS attacks.