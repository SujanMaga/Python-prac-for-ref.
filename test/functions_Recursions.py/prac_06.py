def remove_and_split(string,word):
    newStr = string.replace(word,"")
    return newStr.strip()

this = "               Sujan is a coder 323232     "
n = remove_and_split(this,"Sujan")
print(n)


# to remove a certain word from a string using funtion



# this = "        Sujan is a coder      "
# print(this)
# print(this.strip())
# strip() is used to remove spaces