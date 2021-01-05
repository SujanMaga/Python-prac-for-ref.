nums = [2,32,3,2,2]

it = iter(nums)

print(it.__next__())
print(next(it))


for i in nums:
    print(i)