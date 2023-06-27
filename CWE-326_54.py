#6.# Example 6: Insufficient Authentication

# Vulnerable line:
if username == "admin":
    access_granted = True

# Description: This code is vulnerable to insufficient authentication because it grants access to a user based solely on their username, without any additional verification.