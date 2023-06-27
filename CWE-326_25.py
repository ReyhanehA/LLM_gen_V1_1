#6.# Example 6: Use of input() function without proper input validation

password = input("Enter your password: ") # CWE-326: Insecure use of input() function
if password == "secret":
    print("Access granted!")
else:
    print("Access denied.")