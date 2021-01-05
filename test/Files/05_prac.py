with open('donkey.txt') as f:
    content = f.read()

content = content.replace("donkey","********")

with open('donkey.txt', 'w') as f:
    f.write(content)




# changing a word in a file or censoring the word