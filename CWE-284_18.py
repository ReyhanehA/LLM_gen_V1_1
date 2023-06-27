#9.# Example 9:


import yaml

data = input("Enter some YAML data: ")
yaml.safe_load(data)


# CWE-284: Improper Access Control
# The vulnerable line is line 3, where user input is directly used to parse YAML data without proper validation. An attacker can use this to inject malicious YAML data.