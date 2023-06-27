#6.# Improper Input Validation:


import re

email = input("Enter email: ")

if re.match(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', email):
    print("Valid email address!")
else:
    print("Invalid email address.")

# The vulnerable line is the lack of proper input validation, allowing for various types of input attacks.