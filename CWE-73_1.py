#7.# Example 7:

import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)

email = input("Enter your email address: ")
password = input("Enter your password: ")

server.login(email, password)

# CWE-732: Incorrect Permission Assignment for Critical Resource
# The vulnerable line is line 6, where the user input is being used to authenticate with an email server without proper validation. This can lead to unauthorized access to the email account.