name = input("give me your name ")
age = int(input("now how many rings on that tree of yours?"))
age100 = 100 - age + 2017
print("looking like you'll be a crank around", age100, name)

copycat = input("How many times do you want to hear that again, crank?")
for x in range(int(copycat)):
    print("looking like you'll be a crank around", age100, name)