#6.# Example 6: CWE-321 - Use of Untrusted Input for SQL Query
username = input("Enter your username: ")
password = input("Enter your password: ")
query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"
cursor.execute(query)

# The use of untrusted input in SQL query is vulnerable to SQL injection attacks.