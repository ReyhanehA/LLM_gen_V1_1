#4.# CWE-94: Improper Control of Generation of Code ('Code Injection')
# Vulnerable line: exec(user_input)
user_input = input("Enter Python code to execute: ")
exec(user_input)