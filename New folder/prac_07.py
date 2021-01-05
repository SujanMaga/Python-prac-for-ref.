l1 = [10, 20, 23, 11, 17]
l2 = [13, 43, 24, 36, 12]

def oddEven(l1, l2):
    l3 = []

    for num in l1:
        if num % 2 != 0:
            l3.append(num)

    for num in l2:
        if num % 2 == 0:
            l3.append(num)
    return l3

print(oddEven(l1,l2))

