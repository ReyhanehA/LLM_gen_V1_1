#6.# Improper input validation vulnerability in Python code:


import re

email = input("Enter email address: ")

if re.match(r"[^@]+@[^@]+\.[^@]+", email):
    print("Valid email address")
else:
    print("Invalid email address")

# Vulnerable line: if re.match(r"[^@]+@[^@]+\.[^@]+", email):