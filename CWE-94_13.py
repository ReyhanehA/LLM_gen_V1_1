#4.# Example 4: Path Traversal

# Vulnerable line:
file_path = "/var/www/html/" + filename
with open(file_path, "r") as f:
    contents = f.read()

# Description: This code is vulnerable to path traversal because it concatenates user input directly into a file path without proper sanitization.