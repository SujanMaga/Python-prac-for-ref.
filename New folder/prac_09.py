income = 18000
taxpayable = 0
if income <= 10000:
    taxpayable = 0
elif income <= 20000:
    taxpayable = 10/100 * (income - 10000)
else:
    taxpayable = 10/100*10000
    taxpayable += 20/100* (income - 20000) 
print(taxpayable)
