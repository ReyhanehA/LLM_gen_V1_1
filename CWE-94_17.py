#8.# Example 8: Insecure Randomness

# Vulnerable line:
random_number = random.randint(1, 10)

# Description: This code is vulnerable to insecure randomness because it uses a predictable random number generator.