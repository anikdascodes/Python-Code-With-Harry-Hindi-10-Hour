
a = int(input("Enter your age: "))

# If statement no : 1
if (a%2 == 0):
    print("a is even")
# End of If statement no: 1

# if statement no : 2

if (a>=18):
    print("You are above the age of consent")

elif (a < 0):
    print("You are entering invalid negative age")

elif (a == 0):
    print("You are entering 0 which is not a valid age")

else:
    print("You are bellow the age of consent")


print("End of Program")