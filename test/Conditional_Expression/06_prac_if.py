mark = int(input("Enter your marks "))

if (mark>=90):
    grade = 'A+'
elif (mark>=80):
    grade = 'A'
elif (mark>=70):
    grade = 'B+'
elif (mark>=60):
    grade = 'B'
elif (mark>=50):
    grade = 'C'
else:
    grade = 'Fail'
print(grade)


# To calculate the grade by taking user's input