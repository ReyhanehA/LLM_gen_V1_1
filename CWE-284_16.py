#7.# Example 7:


import pickle

data = input("Enter some pickled data: ")
pickle.loads(data)


# CWE-284: Improper Access Control
# The vulnerable line is line 3, where user input is directly used to unpickle data without proper validation. An attacker can use this to execute arbitrary code.