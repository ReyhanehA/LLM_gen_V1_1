#5.# Code with CWE-78: XPath Injection

from lxml import etree

username = input("Enter username: ")
password = input("Enter password: ")

xml = """
<users>
    <user>
        <username>{}</username>
        <password>{}</password>
    </user>
</users>
""".format(username, password)

root = etree.fromstring(xml)
users = root.xpath("//user[username='{}' and password='{}']".format(username, password))

# Vulnerable line: users = root.xpath("//user[username='{}' and password='{}']".format(username, password))
# Description: This code is vulnerable to XPath injection as it concatenates user input directly into the XPath query without proper sanitization or validation.