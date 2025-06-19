# a = input("Enter the name:")
# b = input("Enter the date:")

# print(f"Dear {a}\nYou are selected\n{b}")


# M2

letter = '''Dear <|Name|>,
you are selected!
<|Date|>'''

print(letter.replace("<|Name|>", "Shubham").replace("<|Date|>", "15 may 2050"))

