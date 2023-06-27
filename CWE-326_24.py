#5.# Example 5: Use of format() function without proper input validation

user_input = input("Enter your name: ")
message = "Hello, {}!".format(user_input) # CWE-326: Insecure use of format() function
print(message)