#10.# Example 10: Use of json module without proper input validation

import json

json_data = input("Enter some JSON data: ")
data = json.loads(json_data) # CWE-326: Insecure use of json module
print(data)