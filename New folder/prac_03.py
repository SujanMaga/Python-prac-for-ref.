def even(str):
    for i in range (0, len(str)-1, 2):
        print(f"index {i} and {str[i]}")


name = 'pynative'

even(name)