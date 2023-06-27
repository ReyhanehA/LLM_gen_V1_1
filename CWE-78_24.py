#5.# Example 5:

import requests

url = input("Enter a URL: ")
response = requests.get(url)

# CWE-78: Improper Neutralization of Special Elements used in an HTTP Header ('HTTP Response Splitting')
# Vulnerable line: response = requests.get(url)
# Description: The user input for url can be manipulated to inject additional HTTP headers.