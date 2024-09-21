# Taking the marks as input from the user
marks = int(input("Enter the marks: "))

# Determining the grade based on the marks
if 90 <= marks <= 100:
    grade = "Ex"
elif 80 <= marks < 90:
    grade = "A"
elif 70 <= marks < 80:
    grade = "B"
elif 60 <= marks < 70:
    grade = "C"
elif 50 <= marks < 60:
    grade = "D"
else:
    grade = "F"

# Output the grade
print(f"The grade for marks {marks} is: {grade}")
