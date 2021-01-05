def greatest(a,b,c):
    if (a>b):
        if (a>c):
            return a
        else:
            return c 
    else:
        if (b>c):
            return b
        else:
            return c        


m = greatest(3,54,5)
print ("The value of greates is: ",m)


# finding greatest number using function