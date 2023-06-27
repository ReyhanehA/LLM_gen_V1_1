#3.# Example 3: CWE-321 - Use of Insecure Random Number Generator
random_number = random.randint(1, 10)

# The use of random.randint() is vulnerable to attacks as it uses a predictable algorithm to generate random numbers.