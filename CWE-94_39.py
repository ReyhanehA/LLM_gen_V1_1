#1.# CWE-94: Improper Control of Generation of Code ('Code Injection')
# Vulnerable line: os.system("ping " + user_input)
import os
user_input = input("Enter IP address to ping: ")
os.system("ping " + user_input)