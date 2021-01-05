# (a+bi)(c+di) = (ac−bd) + (ad+bc)i
class ComplexNumber:

    def __init__(self, r, i):
        self.real = r
        self.imaginary = i

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        realNum = self.real * other.real - self.imaginary * other.imaginary
        ImaginaryNum = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(realNum, ImaginaryNum)

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

c1 = ComplexNumber(3, 2)
c2 = ComplexNumber(1, 7)

print(c1 + c2)
print(c1 * c2)