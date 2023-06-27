#3.# CWE-96: Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')
# Vulnerable line: os.system("ping " + user_input)
import os
user_input = input("Enter an IP address: ")
os.system("ping " + user_input)