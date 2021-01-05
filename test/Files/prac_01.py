f = open('poems.txt')
t = f.read()
if 'twinkle' in t:
    print("twinkle is present")
else:
    print("twinkle is not present")


f.close()

# to find whether a word is present in txt file or not