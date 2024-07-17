import os

# Set the directory path to the root directory
directory_path = "/"

# List the contents of the directory
contents = os.listdir(directory_path)

# Print each item in the directory
for item in contents:
    print(item)