#2.# Example 2: CWE-284 - Improper Access Control

import subprocess

command = "ls -l /path/to/file"
subprocess.call(command, shell=True)

# The vulnerable line is line 3 where the code executes a shell command without checking if the user has permission to access the file.