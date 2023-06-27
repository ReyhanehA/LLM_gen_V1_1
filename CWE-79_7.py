#8.# CWE-79: File Inclusion
# Vulnerable line:
template = open(template_file, "r").read()
output = template.format(**context)

# Description: This code is vulnerable to file inclusion as it includes a file specified by user input without proper validation.