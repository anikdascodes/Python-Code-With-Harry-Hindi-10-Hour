# Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.

d = {}

for i in range(4):
    name = input("Enter friends name: ")
    lang = input("Enter language name: ")

    d.update({name: lang})
    
print(d)