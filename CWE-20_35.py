#10.# Example 10: CWE-20 - Improper Input Validation

import pickle

data = input("Enter pickle data: ")
pickle_data = pickle.loads(data)

# The vulnerable line is line 3, where the input is not validated and can potentially allow for unpickling unintended data.