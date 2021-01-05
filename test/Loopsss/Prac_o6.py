# factorial n!

n = int(input("Enter a number to find a factorial of: "))
sum = 1
for i in range (1, n+1):
    sum = sum*i

print(f"The factorial of number is: {sum}")