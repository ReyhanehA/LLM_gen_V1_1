#7.# Example 7: CWE-284 - Improper Access Control

import xml.etree.ElementTree as ET

file_path = "/path/to/file.xml"
tree = ET.parse(file_path)
root = tree.getroot()

# The vulnerable line is line 3 where the code reads an XML file without checking if the user has permission to access it.