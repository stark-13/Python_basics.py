num = [1,2,3,4,5,4,3,2,1]

def pattern():
    for x in num:
        for y in range(x):
            print("*", end=" ")
        print()

pattern()