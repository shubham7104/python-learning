# Write a program to print multiplication table of a given number using for loop.
# Get input from user
num = int(input("Enter a number to print its multiplication table: "))

# Print multiplication table from 1 to 10
print(f"\nMultiplication Table of {num}:\n")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
