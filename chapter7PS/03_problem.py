# Write a program to print multiplication table of a given number using while loop.
num = int(input("Enter a number to print its multiplication table: "))
print(f"\nMultiplication Table of {num}:\n")

i = 1  # initialize the counter

while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1  # increment to avoid infinite loop
