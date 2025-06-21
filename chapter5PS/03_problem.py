# Can we have a set with 18 (int) and '18' (str) as a value in it?
''' a = {18,}
b = {"18",}
print(type(a))
print(type(b)) '''
s = set()
s.add(18)
s.add("18")
print(s)
