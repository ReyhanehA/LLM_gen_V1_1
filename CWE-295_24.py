#5.# Example 5: CWE-295 - Improper Certificate Validation

import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls(context=ssl._create_unverified_context())

# Vulnerable line: creating an unverified SSL context