# def exponent(base, exp):
#     print(base**exp)

# exponent(2,5)
# exp = non negative
def exponent(base, exp):
    num = exp
    result = 1
    while num > 0:
        result = result * base
        num = num-1
    print(result)

        
        
exponent(2,5)