f = open("file.txt")
# lines = f.readlines() # This will print line as list.
# print(lines, type(lines))
# f.close()
'''
line1 = f.readline()            # .readline() print single line at a time from file.
print(line1, type(line1))       

line2 = f.readline()
print(line2, type(line2))

line3 = f.readline()
print(line3, type(line3))

line4 = f.readline()
print(line4, type(line4))

line5 = f.readline()        # This is just a check what happen if we tell to print the extra line and result is it stop after the line end.
print(line5 == "")          # This means if line5 is equal to or if line5 is empty then print "True"

f.close()
'''
line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()
f.close()