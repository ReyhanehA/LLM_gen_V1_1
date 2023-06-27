#1.# Example 1: Use of eval() function without proper input validation

user_input = input("Enter a mathematical expression: ")
result = eval(user_input) # CWE-23: Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')
print("Result: ", result)