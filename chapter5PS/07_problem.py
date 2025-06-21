'''If the names of 2 friends are same; what will happen to the program in problem
6?'''
d = {}

name = input("Enter Your name: ")
lang = input("Enter the language: ")
d.update({name: lang})
name = input("Enter Your name: ")
lang = input("Enter the language: ")
d.update({name: lang})
name = input("Enter Your name: ")
lang = input("Enter the language: ")
d.update({name: lang})
name = input("Enter Your name: ")
lang = input("Enter the language: ")
d.update({name: lang})

print(d)


# final ans
''' the most recent name's language will remanin and previous one will vansih 'coz we are using ".update" methods'''
