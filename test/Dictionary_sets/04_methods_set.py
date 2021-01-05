a = set()
print(type(a)) 
a.add(3)
a.add(23)
a.add((1,2,43,53,6,9))

print(a) 
# to add value



print(len(a)) 
# finds length of set

# a.remove(23)
# print(a)
# Removes 23 from set
# throws error if it's not availabe in set


print(a.pop())
print(a)