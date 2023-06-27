#7.# Example 7:

import json

json_string = input("Enter a JSON string: ")
data = json.loads(json_string)

# CWE-78: Improper Neutralization of Special Elements used in a JSON String
# Vulnerable line: json.loads(json_string)
# Description: The user input for json_string can be manipulated to inject malicious JSON.