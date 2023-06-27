#6.# Example 6: CWE-284 - Improper Access Control

import json

file_path = "/path/to/file.json"
with open(file_path, "r") as f:
    data = json.load(f)
    print(data)

# The vulnerable line is line 3 where the code reads a JSON file without checking if the user has permission to access it.