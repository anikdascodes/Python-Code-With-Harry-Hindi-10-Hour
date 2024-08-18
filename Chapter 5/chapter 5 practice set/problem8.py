# If languages of two friends are same; what will happen to the program in problem 6?

# If the names of 2 friends are same; what will happen to the program in problem 6?

d = {}

for i in range(4):
    name = input("Enter friends name: ")
    lang = input("Enter language name: ")

    d.update({name: lang})
    
print(d)