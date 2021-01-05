# list1 = ['apple','banana','cherry']
# myit = iter(list1)
# print(next(myit))
# print(next(myit))

class MyNumber:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1

        return x

num = MyNumber()
myiter = iter(num)
print(next(myiter))
print(next(myiter))