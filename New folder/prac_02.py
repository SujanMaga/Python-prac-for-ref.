def numSum():
    pNum = 0
    for i in range(10):
        sum = pNum + i
        print(f"Current number: {i}, Previous number: {pNum}, Sum = {sum}")
        pNum = i

numSum()


