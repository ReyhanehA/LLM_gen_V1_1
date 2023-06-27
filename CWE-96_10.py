#1.# CWE-96: Improper Neutralization of Directives in Statically Saved Code (XSS)

user_input = input("Enter your name: ")
print("Hello " + user_input + "!")

# The vulnerable line is line 2 where user input is directly concatenated with a string without proper sanitization, allowing for potential XSS attacks.