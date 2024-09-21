# Define the list of names
names = ["Alice", "Bob", "Charlie", "David", "Eve"]

# Taking the name as input from the user
name_to_check = input("Enter the name to check: ")

# Checking if the name is present in the list
if name_to_check in names:
    print(f"{name_to_check} is present in the list.")
else:
    print(f"{name_to_check} is not present in the list.")
