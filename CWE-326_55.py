#7.# Example 7: Insufficient Authorization

# Vulnerable line:
if user_role == "admin":
    delete_file(filename)

# Description: This code is vulnerable to insufficient authorization because it allows a user with a certain role to perform actions that they should not be allowed to do.