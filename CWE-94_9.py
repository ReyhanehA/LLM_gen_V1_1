#10.# CWE-94: Improper Control of Generation of Code ('Code Injection')
# Vulnerable line: eval(os.getenv(user_input))
import os
user_input = input("Enter an environment variable to evaluate: ")
eval(os.getenv(user_input))