#6.# Example 6: XML Injection

import xml.etree.ElementTree as ET

username = input("Enter username: ")

root = ET.Element("user")
root.set("name", username)

# CWE-78: The user input is not properly sanitized and can be used to inject XML tags
# Vulnerable line: root.set("name", username)