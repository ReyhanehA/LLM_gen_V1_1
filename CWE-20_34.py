#9.# Example 9: CWE-20 - Improper Input Validation

import xml.etree.ElementTree as ET

xml_data = input("Enter XML data: ")
root = ET.fromstring(xml_data)

# The vulnerable line is line 3, where the input is not validated and can potentially allow for parsing unintended XML data.