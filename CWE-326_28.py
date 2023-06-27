#9.# Example 9: Use of xml.etree.ElementTree module without proper input validation

import xml.etree.ElementTree as ET

xml_data = input("Enter some XML data: ")
root = ET.fromstring(xml_data) # CWE-326: Insecure use of xml.etree.ElementTree module
print(root.tag)