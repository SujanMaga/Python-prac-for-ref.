words = ["donkey","Mote","kaley"]


with open('donkey.txt') as f:
    content = f.read()




for word in words:
    content = content.replace(word,"********")
    with open('donkey.txt', 'w') as f:
        f.write(content)




# changing multiple words in a file or censoring the word