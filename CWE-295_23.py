#4.# Example 4: CWE-295 - Improper Certificate Validation

import http.client

conn = http.client.HTTPSConnection('example.com', context=ssl._create_unverified_context())

# Vulnerable line: creating an unverified SSL context