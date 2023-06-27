#10.# Example 10: CWE-321 - Use of Unvalidated Input for Regular Expression
pattern = input("Enter the regular expression pattern: ")
re.findall(pattern, data)

# The use of unvalidated input for regular expression is vulnerable to regular expression denial of service (ReDoS) attacks.