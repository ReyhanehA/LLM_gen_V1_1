#5.# CWE-96: Improper Neutralization of Directives in Statically Saved Code (XSS)

import json

data = input("Enter some JSON data: ")
parsed_data = json.loads(data)

print("Name: " + parsed_data['name'])
print("Age: " + parsed_data['age'])

# The vulnerable line is line 2 where user input is directly used in a JSON object without proper sanitization, allowing for potential XSS attacks.