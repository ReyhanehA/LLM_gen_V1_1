#4.# CWE-96: Improper Neutralization of Script-Related HTML Tags in a Web Page (Basic XSS)
# Vulnerable line: print("<script>alert('" + user_input + "');</script>")
user_input = input("Enter your name: ")
print("<script>alert('" + user_input + "');</script>")