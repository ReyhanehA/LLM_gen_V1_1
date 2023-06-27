#1.# Example 1: Improper Input Validation

input_data = input("Enter your age: ")
if input_data.isdigit():
    age = int(input_data)
    if age < 18:
        print("You are not old enough to vote.")
    else:
        print("You are old enough to vote.")
else:
    print("Invalid input.")

# The vulnerable line is line 2 where input_data is not properly validated before being used.
# CWE-20: Improper Input Validation