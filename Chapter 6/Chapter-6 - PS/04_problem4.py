# Taking the username as input from the user
username = input("Enter your username: ")

# Checking the length of the username
if len(username) < 10:
    print("The username contains less than 10 characters.")
else:
    print("The username contains 10 or more characters.")
