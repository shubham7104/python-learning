st = "Hey Shubham you are amazing"

f = open("myfile.txt", "a") # It will automatic(if file not exist before) create and open in append(means adding the line at last) mode.

f.write(st)# It will write the "sr" in the file.

f.close() # It will close the file.