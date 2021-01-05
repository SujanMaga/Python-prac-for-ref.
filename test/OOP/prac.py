def div(a,b):
    print (a/b)

def specialDiv(func):
    def inner (a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner

div1 = specialDiv(div)
div1(2,4)

# decorators