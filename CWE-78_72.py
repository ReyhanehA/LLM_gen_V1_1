#6.# Improper Input Validation:


import re

email = input("Enter email address: ")
if re.match(r"[^@]+@[^@]+\.[^@]+", email):
    print("Valid email address!")
else:
    print("Invalid email address!")


# The vulnerable line is line 2, where user input is not properly validated against a regular expression, allowing for input validation attacks.