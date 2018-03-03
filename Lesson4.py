number = int(input("Give me a number: "))

x = range(1, number)

yes = []

for num in x:
    if number % num == 0:
        yes.append(num)

print(yes)