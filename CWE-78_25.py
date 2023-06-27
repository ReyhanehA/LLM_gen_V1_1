#6.# Example 6:

import xml.etree.ElementTree as ET

xml_string = input("Enter an XML string: ")
root = ET.fromstring(xml_string)

# CWE-78: Improper Neutralization of Special Elements used in an XML Comment
# Vulnerable line: None
# Description: The user input for xml_string can be manipulated to inject malicious XML comments.