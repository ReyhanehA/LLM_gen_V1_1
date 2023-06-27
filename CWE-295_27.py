#8.# Example 8: CWE-295 - Improper Certificate Validation

import poplib

mail = poplib.POP3_SSL('pop.gmail.com', context=ssl._create_unverified_context())

# Vulnerable line: creating an unverified SSL context