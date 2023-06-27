#8.# Code with CWE-78: Command Injection via Shell Metacharacters

import subprocess

filename = input("Enter filename: ")
subprocess.call("cat " + filename, shell=True)

# Vulnerable line: subprocess.call("cat " + filename, shell=True)
# Description: This code is vulnerable to command injection via shell metacharacters as it concatenates user input directly into the shell command without proper validation or sanitization.