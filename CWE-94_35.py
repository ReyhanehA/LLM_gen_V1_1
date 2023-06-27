#7.# Example 7: CWE-94 - Improper Control of Generation of Code ('Code Injection')

import pickle

user_input = input("Enter a pickle string: ")
data = pickle.loads(user_input)

# The vulnerable line is data = pickle.loads(user_input)
# This code allows an attacker to inject arbitrary Python code into the system by manipulating the user_input variable.