#8.# Example 8: CWE-321 - Use of Untrusted Input for File Operations
filename = input("Enter the filename: ")
with open(filename, "r") as f:
    data = f.read()

# The use of untrusted input for file operations is vulnerable to attacks as it can be used to access or modify sensitive files.