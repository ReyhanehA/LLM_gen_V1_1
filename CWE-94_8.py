#9.# CWE-94: Improper Control of Generation of Code ('Code Injection')
# Vulnerable line: os.system(input())
import os
os.system(input("Enter a command to execute: "))