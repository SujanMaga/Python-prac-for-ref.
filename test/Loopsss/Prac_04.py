num = int(input("Enter a number: "))
prime = True

for i in range(2,num):
    if (num%i == 0):
        prime = False
        break

if prime is True:
    print("The given number is prime")
else:
    print("The given number isn't prime")     