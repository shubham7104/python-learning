d = {} # Empty dict.
marks = {
    "Shubham": 100,
    "Harry": 56,
    "Rohan": 23,
    0: "Shubham"
}

# print(marks.items()) # It print the all items in fome of tuples.
# print(marks.keys()) # It print the all keys in fome of tuples.
# marks.update({"Shubham": 99, "Saurab": 100}) # It updates the marks.
# print(marks)

print(marks.get("Shubham2")) # print none as shubham2 key dont exists.
print(marks.get("Harry"))
print(marks["Harry2"]) # print invalid 'coz "Harry2" index is not present.
