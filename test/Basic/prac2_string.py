# name = input("Enter your name")
# print("Good morning,",name)

letter = '''Dear <|NAME|>,
You are selected!

Date: <|DATE|>
'''
name = input("Enter name here\n")
date = input("Enter date\n")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)
# Template for mail