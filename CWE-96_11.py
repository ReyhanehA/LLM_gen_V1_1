#2.# CWE-96: Improper Neutralization of Directives in Statically Saved Code (XSS)

import cgi

form = cgi.FieldStorage()
name = form.getvalue('name')

print("Hello " + name + "!")

# The vulnerable line is line 4 where user input is directly concatenated with a string without proper sanitization, allowing for potential XSS attacks.