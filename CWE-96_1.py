#2.# CWE-96: Improper Neutralization of Directives in Dynamically Evaluated Code ('Eval Injection')
# Vulnerable line: eval(user_input)
user_input = input("Enter a mathematical expression: ")
result = eval(user_input)
print(result)