dic = {
    'batti' : 'light',
    'pankha' : 'fan',
    'khanu' : 'eat',
    'sutnu' : 'sleep'
}
print("Options are: ",dic.keys())
a = input("Enter the Nepali word \n")
print("The meaning fo the word is:",dic.get(a))
# the above line will not thorw error if key is not availabe in dictionary

# to take user value of nepali word and convert in english