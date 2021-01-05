myDict = {
    'fast': 'very rapidly',
    'magnificant' : 'wonderful',
    'marks' : [1,3,44],
    'myDict1': {'namaste': 'greeting'},
    1: 2
}

print(list(myDict.keys()))
# typecasting to change to list from dic.



print(myDict.keys())
# prints keys of dic.
print(myDict.values())
# prints values of dictonary
print(type(myDict.keys()))
# to know type

print(myDict.items())
# returns a list of (Key, value) tuples

print(myDict)
updateDict = {
    "coca-cola" : "cold drink"
}
myDict.update(updateDict)
print(myDict)
# Updates or adds content in the dictionary by adding key-value pair

# difference between .get and [ ]syntax
# print(myDict.get("coca-cola1")) #reurns none a coca-cola1 is not present in the dic.
# print(myDict["coca-cola1"])  #throws an error as it is not present.



