
# Use open funtion to read content of a file

f = open('sample.txt', 'r')
# f = open('sample.txt') By default is read
data = f.read(5)
print(data)
f.close()

