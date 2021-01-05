n = [10, 20, 33, 46, 55]

def divByFive(list1):
    print("Given list is ",list1 )
    print("Divisible of 5 in list")
    for num in list1:
        if (num % 5 == 0):
            print(num)


divByFive(n)
