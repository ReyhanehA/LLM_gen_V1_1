#4.# Example 4: CWE-94 - Improper Control of Generation of Code ('Code Injection')

import json

user_input = input("Enter a JSON string: ")
data = json.loads(user_input)

# The vulnerable line is data = json.loads(user_input)
# This code allows an attacker to inject arbitrary JSON code into the system by manipulating the user_input variable.