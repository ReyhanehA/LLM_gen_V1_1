#8.# Example 8:


import xml.etree.ElementTree as ET

data = input("Enter some XML data: ")
root = ET.fromstring(data)


# CWE-284: Improper Access Control
# The vulnerable line is line 3, where user input is directly used to parse XML data without proper validation. An attacker can use this to inject malicious XML data.