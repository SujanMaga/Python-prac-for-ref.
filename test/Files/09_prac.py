with open('this.txt') as f:
    content = f.read()

with open('copy.txt','w') as f:
    f.write(content)


# To make the copy of a file