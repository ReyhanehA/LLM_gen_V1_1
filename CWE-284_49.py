#10.# Example 10: Insufficient Input Validation

import re

email = input("Enter email: ")

if re.match(r"[^@]+@[^@]+\.[^@]+", email):
    print("Valid email")
else:
    # Vulnerable line: print("Invalid email")
    # Description: This code has insufficient input validation as it does not check for special characters or length of the email address.
    print("Invalid email")