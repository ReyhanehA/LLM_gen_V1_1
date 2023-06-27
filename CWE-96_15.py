#6.# CWE-96: Improper Neutralization of Directives in Statically Saved Code (XSS)

import xml.etree.ElementTree as ET

xml_data = input("Enter some XML data: ")
root = ET.fromstring(xml_data)

print("Name: " + root.find('name').text)
print("Age: " + root.find('age').text)

# The vulnerable line is line 2 where user input is directly used in an XML object without proper sanitization, allowing for potential XSS attacks.