def getLine():
    while True:
        line = input("Give me a sentence: ")
        if not len(line.split()) > 1:
            print("Needs to be at least two words in the sentence")
            continue
        else:
            break
    return line

def reverseLine(line):
    myList = line.split()
    newLine = " ".join(myList[::-1])
    return newLine

line = getLine()
print(reverseLine(line))