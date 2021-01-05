content = True
i = 1
with open('logfile.txt') as f:
    while content:
        content = f.readline()

        if 'Python' in content:
            print(content) 
            print(f"Yes, Python is present on line number {i}")
        i = i+1





# to find a line number in a log file.