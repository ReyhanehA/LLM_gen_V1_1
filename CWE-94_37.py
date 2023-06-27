#9.# Example 9: CWE-94 - Improper Control of Generation of Code ('Code Injection')

import urllib.request

user_input = input("Enter a URL: ")
response = urllib.request.urlopen(user_input)

# The vulnerable line is response = urllib.request.urlopen(user_input)
# This code allows an attacker to inject arbitrary URLs into the system by manipulating the user_input variable.