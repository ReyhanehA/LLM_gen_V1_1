#6.# Improper Input Validation:


import re

email = input("Enter email: ")
if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
    print("Invalid email address")

# The vulnerable line is the regular expression where user input is not properly validated, allowing for improper input validation.