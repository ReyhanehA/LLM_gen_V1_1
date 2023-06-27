#5.# Example 5:


import subprocess

command = input("Enter a command: ")
subprocess.call(command)


# Vulnerable line: line 3
# Description: This code is vulnerable to CWE-284 (Improper Access Control) because it does not properly validate the user's input. An attacker could enter a malicious command and potentially execute arbitrary code on the system.