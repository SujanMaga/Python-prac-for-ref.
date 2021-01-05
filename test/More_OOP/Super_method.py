class Parent:
    def __init__(self, name):
        print("Parent __init__", name)

class Parent1:
    def __init__(self, name):
        print("Parent __init__", name)


class Child(Parent, Parent1):
    def __init__(self):
        print("Child __init__")
        super().__init__('Sujan')
        Parent1.__init__(self, "tom")


child = Child()
print(Child.__mro__)