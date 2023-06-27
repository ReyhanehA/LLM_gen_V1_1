#9.# Example 9: CWE-321 - Use of Unsanitized Input for SQL Queries
username = input("Enter your username: ")
password = input("Enter your password: ")
query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"
cursor.execute(query)

# The use of unsanitized input for SQL queries is vulnerable to attacks as it can be used to inject malicious SQL code.