#6.# Example 6: CWE-94 - Improper Control of Generation of Code ('Code Injection')

import yaml

user_input = input("Enter a YAML string: ")
data = yaml.load(user_input)

# The vulnerable line is data = yaml.load(user_input)
# This code allows an attacker to inject arbitrary YAML code into the system by manipulating the user_input variable.