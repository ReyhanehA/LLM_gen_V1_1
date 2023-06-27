#3.# Example 3: Use of pickle module without proper input validation

import pickle

data = input("Enter some data: ")
with open("data.pickle", "wb") as f:
    pickle.dump(data, f) # CWE-326: Insecure use of pickle module