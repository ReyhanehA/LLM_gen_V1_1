#7.# Example 7: CWE-20 - Improper Input Validation

import csv

filename = input("Enter a filename: ")
with open(filename, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# The vulnerable line is line 3, where the input is not validated and can potentially allow for accessing unintended files.