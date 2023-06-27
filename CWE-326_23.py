#4.# Example 4: Use of exec() function without proper input validation

user_input = input("Enter some Python code: ")
exec(user_input) # CWE-326: Insecure use of exec() function