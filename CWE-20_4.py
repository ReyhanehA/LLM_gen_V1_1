#9.# Example 9: XML Injection

import xml.etree.ElementTree as ET

root = ET.Element("root")
child = ET.SubElement(root, "child")
child.text = input("Enter some text: ")
ET.dump(root)

# The vulnerable line is line 4 where user input is used to construct an XML element
# CWE-20: Improper Input Validation
# This code is vulnerable to XML injection attacks as it does not properly sanitize user input