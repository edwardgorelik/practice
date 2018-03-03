list = [1,8,3,21,6,9,3,1,4,10]
check = int(input("give me a number: "))
new_list = []
for element in list:
    if element < check:
        new_list.append(element)


print(new_list)