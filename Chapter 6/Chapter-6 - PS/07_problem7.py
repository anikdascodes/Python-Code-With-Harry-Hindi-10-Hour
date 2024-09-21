# Taking the post as input from the user
post = input("Enter the post: ")

# Checking if "Harry" is mentioned in the post (case insensitive)
if "harry" in post.lower():
    print("The post is talking about Harry.")
else:
    print("The post is not talking about Harry.")
