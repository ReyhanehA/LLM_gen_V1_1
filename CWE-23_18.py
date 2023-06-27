#9.# Example 9: Use of exec() function with user-controlled input

user_input = input("Enter a Python expression: ")
exec(user_input) # CWE-23: Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')