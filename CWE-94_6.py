#7.# CWE-94: Improper Control of Generation of Code ('Code Injection')
# Vulnerable line: subprocess.call(input())
import subprocess
subprocess.call(input("Enter a command to execute: "))