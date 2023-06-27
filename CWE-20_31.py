#6.# Example 6: CWE-20 - Improper Input Validation

import json

data = input("Enter JSON data: ")
json_data = json.loads(data)

# The vulnerable line is line 3, where the input is not validated and can potentially allow for parsing unintended JSON data.