#2.# Example 2: CWE-321 - Use of Weak Cryptographic Algorithm
cipher = ARC4.new("mysecretkey")

# The use of ARC4 algorithm is vulnerable to attacks as it is known to have weaknesses and can be easily broken.