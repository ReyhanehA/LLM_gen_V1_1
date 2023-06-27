#8.# Example 8: CWE-94 - Improper Control of Generation of Code ('Code Injection')

import csv

user_input = input("Enter a CSV file name: ")
with open(user_input, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# The vulnerable line is with open(user_input, 'r') as f:
# This code allows an attacker to inject arbitrary file names into the system by manipulating the user_input variable.