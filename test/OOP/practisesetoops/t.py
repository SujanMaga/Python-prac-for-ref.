# (a+bi)(c+di) = (ac-bd) + (ad+bc)i
# (a+bi)+(c+di)= (a+c) + (b+d)i

class Complex:
    def __init__(self, r, i):
        self.real = r
        self.imaginary = i

    def __str__(self):
        if self.imaginary<0:
            return f"{self.real} - {-self.imaginary}i"
        else:
            return f"{self.real} + {self.imaginary}i"

    def __add__(self,other):
        return f"{self.real+other.real} + {self.imaginary+other.imaginary}i "
    
    def __mul__(self, other):
        real = (self.real * other.real )- (self.imaginary * other.imaginary)
        imaginary = (self.real * other.imaginary)+(self.imaginary * other.real)
        return Complex(real , imaginary)

c1 = Complex(3,10)
c2 = Complex(5,7)
print(c1)
print(c2)
print(c1*c2)
c3 = Complex(2,-5)
print(c3)

