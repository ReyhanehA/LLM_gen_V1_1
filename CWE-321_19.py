#10.# CWE-321: Use of Hard-coded File Path
# Vulnerable line: file_path = "/home/user/myfile.txt"
with open(file_path, "r") as f:
    data = f.read()