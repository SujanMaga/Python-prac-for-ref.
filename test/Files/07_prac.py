with open('logfile.txt') as f:
    content = f.read()

if 'Python' in content:
    print("yes, python is present")     
else:
    print("no, python is not present")


# to find a word in a log file.