a = int(input("Enter your age: "))

# if elif else ladder

if (a>=18):
    print("You are above the age of consent")

elif (a < 0):
    print("You are entering invalid negative age")

elif (a == 0):
    print("You are entering 0 which is not a valid age")

else:
    print("You are bellow the age of consent")


print("End of Program")