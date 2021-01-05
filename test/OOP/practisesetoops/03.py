class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        str = ""
        index = 0
        for i in self.vec:
            str += f" {i}a{index} +"
            index += 1
        return str[0:-1]

    def __add__(self, vec2):
        newList = []
        for i in range (len(self.vec)):
            newList.append(self.vec[i] + vec2.vec[i])
        return Vector(newList)
        
    def __mul__(self,vec2):
        product = 0
        for i in range (len(self.vec)):
            product += self.vec[i] * vec2.vec[i]
        return product

vec1 = Vector([4,2,5,6])
vec2 = Vector([42,3,412,87])
print(vec1)
print(vec2)
print(vec1+vec2)
print(vec1*vec2)

