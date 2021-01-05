# n = 4
# product = 1
# for i in range(n+1):
#     product =product * (i+1)
# print(product)    

def factorial_inter(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product

f = factorial_inter(5)
print(f)        
     
def factorial_recursive(n):
    if n == 1 or n==0:
        return 1
    else:    
        return n * factorial_recursive(n-1)


f1 = factorial_recursive(4)
print(f1)