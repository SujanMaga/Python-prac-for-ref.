import os
os.getcwd()
os.chdir('D:\\python\\test\\Files')


f = open('sample.txt', 'r')

# prints first line
data = f.readline()  
print(data)

# prints second line
data = f.readline()
print(data)


# prints third line
data = f.readline()
print(data)


f.close()

