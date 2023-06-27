#5.# CWE-94: Improper Control of Generation of Code ('Code Injection')
# Vulnerable line: os.system("rm " + user_input)
import os
user_input = input("Enter a file name to delete: ")
os.system("rm " + user_input)