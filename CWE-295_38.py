#9.# Example 9: CWE-295 - Improper Certificate Validation

import xmlrpc.client

server = xmlrpc.client.ServerProxy('https://example.com', context=ssl._create_unverified_context())

# Vulnerable line: creating an unverified SSL context