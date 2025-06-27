'''Write a program to find whether a given username contains less than 10
characters or not.'''
username = input("Enter username: ")
 
if(len(username)<10):
    pirnt("Your username contain less than 10 chracters")
else:
    print("Your username contain more or equal to than 10 chracters")