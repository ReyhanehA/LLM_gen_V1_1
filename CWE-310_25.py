#6.# Example 6: CWE-310 - Cryptographic Issues

import random

key = str(random.randint(100000, 999999))
print("Your OTP key is: " + key) # CWE-310: Generating OTP keys using random number generators can lead to security vulnerabilities