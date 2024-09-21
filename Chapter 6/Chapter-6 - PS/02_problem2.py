# Taking input from the user for marks in 3 subjects
marks1 = int(input("Enter marks 1: "))
marks2 = int(input("Enter marks 2: "))
marks3 = int(input("Enter marks 3: "))

# Checking for total percentage
total_percentage = (marks1 + marks2 + marks3) / 300 * 100

# Checking if the student has at least 33% in each subject and 40% overall
if total_percentage >= 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33:
    print("The student has passed.")
else:
    print("The student has failed.")
