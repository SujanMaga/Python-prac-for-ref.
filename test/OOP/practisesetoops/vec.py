class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __add__(self, other):
        newList = []
        for i in range(len(self.vec)):
            newList.append(self.vec[i]+other.vec[i])
        return Vector(newList)

    def __str__(self):
        str = ""
        index = 0
        for i in self.vec:
            str += f" {i}a{index} +"
            index += 1
        return str[0:-1]


    def __mul__(self, other):
        sum = 0
        for i in range(len(self.vec)):
            sum += self.vec[i] * other.vec[i]
        return sum

v1 = Vector([3,5,6])
v2 = Vector([6,5,6])

print(v1)
print(v2)
print(v1+v2)
print(v1*v2)
