#10.# Example 10:


import csv

filename = input("Enter a filename: ")
with open(filename, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


# CWE-284: Improper Access Control
# The vulnerable line is line 2, where user input is used to construct a file path without proper validation. An attacker can use this to read arbitrary CSV files on the system.