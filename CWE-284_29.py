#10.# Example 10: CWE-284 - Improper Access Control

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("example.com", username="user", password="password")
sftp = ssh.open_sftp()
file_path = "/path/to/file"
with sftp.open(file_path, "r") as f:
    print(f.read())

# The vulnerable line is line 8 where the code reads a file from a remote server over SSH without checking if the user has permission to access it.