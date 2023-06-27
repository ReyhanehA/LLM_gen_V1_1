#1.# CWE-96: Improper Neutralization of Directives in Statically Saved Code ('Static Code Injection')
# Vulnerable line: os.system("echo " + user_input)
import os
user_input = input("Enter your name: ")
os.system("echo " + user_input)