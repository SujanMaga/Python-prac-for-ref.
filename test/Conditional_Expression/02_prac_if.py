m1 = int(input("Enter marks of Math"))
m2 = int(input("Enter marks of Science"))
m3 = int(input("Enter marks of Nepali"))

if (m1<33 or m2<33 or m3<33):
    print("You are fail due to less marks in a subject")
elif (m1+m2+m3)/3 <40:
    print("You are fail due to less than 40%")
else:
    print("Congratulations! You have passed the test")

# program to calculate the result of a student