#7.# Example 7: Insecure Randomness

import random

password = str(random.randint(1000, 9999))

# Vulnerable line: password = str(random.randint(1000, 9999))
# Description: This code is vulnerable to insecure randomness as it uses the default random number generator which may not be cryptographically secure.