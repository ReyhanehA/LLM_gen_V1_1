#6.# Insecure Randomness Vulnerability:

# Vulnerable line:
random_number = random.randint(1, 10)

# Description: This code is vulnerable to insecure randomness as it uses the default random number generator, which is not cryptographically secure and can be easily predicted by an attacker.