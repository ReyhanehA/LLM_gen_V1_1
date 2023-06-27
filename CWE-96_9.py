#10.# CWE-96: Improper Neutralization of Special Elements used in an XML Comment ('XML Injection')
# Vulnerable line: print("<!--" + user_input + "-->")
user_input = input("Enter an XML comment: ")
print("<!--" + user_input + "-->")