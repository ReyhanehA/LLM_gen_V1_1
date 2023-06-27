#5.# CWE-96: Improper Neutralization of Script-Related HTML Tags in a Web Page (DOM-Based XSS)
# Vulnerable line: document.write("<script>alert('" + user_input + "');</script>")
user_input = input("Enter your name: ")
document.write("<script>alert('" + user_input + "');</script>")