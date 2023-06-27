#1.# Example 1: CWE-295 - Improper Certificate Validation

import ssl

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

# Vulnerable line: disabling certificate validation