#5.# Example 5: CWE-94 - Improper Control of Generation of Code ('Code Injection')

import xml.etree.ElementTree as ET

user_input = input("Enter an XML string: ")
root = ET.fromstring(user_input)

# The vulnerable line is root = ET.fromstring(user_input)
# This code allows an attacker to inject arbitrary XML code into the system by manipulating the user_input variable.