def listTaker(myList):
    taker = len(myList)
    newList = []
    newList.append(myList[0])
    newList.append(myList[taker - 1])
    return newList


a = [5, 10, 15, 20, 25]
b = listTaker(a)
print(b)


