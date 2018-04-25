def buildSet():
    basic = []
    while True:
        try:
            loops = int(input("How many items are you putting into the list?"))
        except ValueError:
            print("Input must be a number")
            continue
        else:
            break
    for x in range(0, loops):
        growth = input("What are you putting into the list?")
        basic.append(growth)
    return basic

def rebuild(myList = []):
    newSet = set(myList)
    return newSet


temp = buildSet()
print(temp)
theSet = rebuild(temp)
print(theSet)



