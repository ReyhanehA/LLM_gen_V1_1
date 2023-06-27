#4.# Example 4: Use of exec() function without proper input validation

user_input = input("Enter a Python expression: ")
exec(user_input) # CWE-23: Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')