#5.# Example 5: CWE-284 - Improper Access Control

import csv

file_path = "/path/to/file.csv"
with open(file_path, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# The vulnerable line is line 3 where the code reads a CSV file without checking if the user has permission to access it.