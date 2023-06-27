#6.# Example 6: Use of eval() function with user-controlled input

user_input = input("Enter a Python expression: ")
result = eval(user_input) # CWE-23: Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')
print("Result: ", result)