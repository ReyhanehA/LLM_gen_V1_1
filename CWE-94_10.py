#1.# Example 1: SQL Injection

# Vulnerable line: 
query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"

# Description: This code is vulnerable to SQL injection because it concatenates user input directly into a SQL query without proper sanitization.