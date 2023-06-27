#10.# Example 10: CWE-94 - Improper Control of Generation of Code ('Code Injection')

import ftplib

user_input = input("Enter an FTP server address: ")
ftp = ftplib.FTP(user_input)

# The vulnerable line is ftp = ftplib.FTP(user_input)
# This code allows an attacker to inject arbitrary FTP server addresses into the system by manipulating the user_input variable.