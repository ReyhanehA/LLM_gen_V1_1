#9.# CWE-96: Improper Neutralization of Special Elements used in a Regular Expression ('Regular Expression Injection')
# Vulnerable line: re.findall(user_input, "Hello, World!")
import re
user_input = input("Enter a regular expression: ")
result = re.findall(user_input, "Hello, World!")
print(result)