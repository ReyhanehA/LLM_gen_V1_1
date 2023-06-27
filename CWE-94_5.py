#6.# CWE-94: Improper Control of Generation of Code ('Code Injection')
# Vulnerable line: eval(input())
result = eval(input("Enter a mathematical expression: "))
print(result)