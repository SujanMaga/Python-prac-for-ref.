def func(number):
    num = number
    print("original number: ", number)
    reverseNum = 0
    while num > 0:
        reminder = num % 10
        reverseNum = (reverseNum * 10) + reminder
        num = num // 10

    if number == reverseNum:
        print("The original number and reversed number is same.")
    else:
        print("The original number and reversed number is not same.")

func(121)




