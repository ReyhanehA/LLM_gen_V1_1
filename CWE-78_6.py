#7.# Code with CWE-78: Header Injection

import smtplib

to = input("To: ")
subject = input("Subject: ")
body = input("Body: ")

msg = "To: {}\nSubject: {}\n\n{}".format(to, subject, body)
server = smtplib.SMTP('smtp.gmail.com', 587)
server.sendmail('me@gmail.com', to, msg)

# Vulnerable line: msg = "To: {}\nSubject: {}\n\n{}".format(to, subject, body)
# Description: This code is vulnerable to header injection as it concatenates user input directly into the email message without proper sanitization or validation.