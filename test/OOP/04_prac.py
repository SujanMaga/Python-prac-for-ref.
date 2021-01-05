class Sample:
    a = "Sujan"


obj = Sample() 
obj.a = "Anuska"

Sample.a = "Sharon"
# to change class attribute


print(Sample.a)
print(obj.a)


# no, it doesn't change class attribute