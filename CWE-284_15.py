#6.# Example 6:


import json

data = input("Enter some JSON data: ")
json.loads(data)


# CWE-284: Improper Access Control
# The vulnerable line is line 3, where user input is directly used to parse JSON data without proper validation. An attacker can use this to inject malicious JSON data.