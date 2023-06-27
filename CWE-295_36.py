#7.# Example 7: CWE-295 - Improper Certificate Validation

import imaplib

mail = imaplib.IMAP4_SSL('imap.gmail.com', context=ssl._create_unverified_context())

# Vulnerable line: creating an unverified SSL context