#7.# Example 7: OS Command Injection

import subprocess

filename = input("Enter filename: ")

# CWE-78: The user input is not properly sanitized and can be used to inject OS commands
# Vulnerable line: subprocess.call(["cat", filename])
subprocess.call(["cat", os.path.join('/home/user/files', filename)])