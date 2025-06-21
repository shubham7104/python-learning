'''What will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?'''
s = set()
s.add(20)
s.add(20.0)
s.add('20')
print(len(s)) # The output will 2 'coz python compares the value; not the data type. For python 20 == 20.0 is True.(same)
print(s)
