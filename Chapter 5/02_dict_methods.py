marks = {
    "Harry" : 100,
    "Subham" : 56,
    0: "Harry"
}

print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({"Harry":99, "Renuka":100})
print(marks)

print(marks.get("Harry2")) # prints none 
print(marks["Harry2"]) # return error