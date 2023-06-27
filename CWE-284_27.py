#8.# Example 8: CWE-284 - Improper Access Control

import pickle

file_path = "/path/to/file.pkl"
with open(file_path, "rb") as f:
    data = pickle.load(f)
    print(data)

# The vulnerable line is line 3 where the code reads a pickled object file without checking if the user has permission to access it.