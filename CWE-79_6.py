#7.# CWE-79: XML Injection
# Vulnerable line:
xml = "<user><name>" + username + "</name><email>" + email + "</email></user>"

# Description: This code is vulnerable to XML injection as it concatenates user input directly into an XML document without proper encoding.