#9.# Example 9: CWE-321 - Use of Unvalidated Input for Command Execution
command = input("Enter the command: ")
os.system(command)

# The use of unvalidated input for command execution is vulnerable to command injection attacks.