#7.# Example 7: CWE-321 - Use of Unvalidated Input for File Operations
filename = input("Enter the filename: ")
with open(filename, "r") as file:
    data = file.read()

# The use of unvalidated input for file operations is vulnerable to directory traversal attacks.