#8.# CWE-96: Improper Neutralization of Special Elements used in an XPath Expression ('XPath Injection')
# Vulnerable line: tree.xpath("//book[author='" + user_input + "']/title")
from lxml import etree
user_input = input("Enter an author name: ")
xml = """
<library>
    <book>
        <title>Python for Beginners</title>
        <author>John Smith</author>
    </book>
    <book>
        <title>Java Programming</title>
        <author>Jane Doe</author>
    </book>
</library>
"""
tree = etree.fromstring(xml)
result = tree.xpath("//book[author='" + user_input + "']/title")
print(result)