#6.# Example 6: CWE-295 - Improper Certificate Validation

import ftplib

ftp = ftplib.FTP_TLS('example.com')
ftp.auth_tls(context=ssl._create_unverified_context())

# Vulnerable line: creating an unverified SSL context