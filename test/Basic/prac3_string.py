# # program to detect double spaces in a string (Simple)
# st = "Namaste, my name is Sujan. I am currently studying nothing. Here's the double space   Ok thank you"
# doubleSpaces = st.find("  ")
# print(doubleSpaces)

# replace double space with single space
st = "Namaste, my name is Sujan. I am currently studying nothing. Here's the double space    Ok thank you"
doubleSpaces = st.find("  ")
st = st.replace("  "," ")
print(st)


