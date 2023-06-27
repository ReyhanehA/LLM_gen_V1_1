#3.# Example 3: CWE-295 - Improper Certificate Validation

import urllib.request

opener = urllib.request.build_opener()
opener.add_handler(urllib.request.HTTPSHandler(context=ssl._create_unverified_context()))

# Vulnerable line: creating an unverified SSL context