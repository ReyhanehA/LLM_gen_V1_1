#2.# Example 2: CWE-295 - Improper Certificate Validation

import requests

response = requests.get('https://example.com', verify=False)

# Vulnerable line: disabling certificate validation