#10.# Example 10: CWE-321 - Use of Unvalidated Input for Command Execution
command = input("Enter the command: ")
os.system(command)

# The use of unvalidated input for command execution is vulnerable to attacks as it can be used to execute malicious commands.