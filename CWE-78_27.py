#8.# Example 8:

import pickle

data = input("Enter some data: ")
serialized_data = pickle.dumps(data)

# CWE-78: Improper Neutralization of Special Elements used in a Serialized Object
# Vulnerable line: pickle.dumps(data)
# Description: The user input for data can be manipulated to execute arbitrary code when deserialized.