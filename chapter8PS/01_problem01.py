# Write a program using functions to find greatest of three numbers.
def greatest(a, b, c):
    if(a>b and b>c):
        return(a)
    elif(b>a and b>c):
        return(b)
    elif(c>a and c>b):
        return(c)
a = 1
b = 2
c = 3
print(greatest(a, b, c))