import random

a = random.sample(range(1000),50)
b = random.sample(range(1000),50)

c = []

for num in a:
    if num in b:
        c.append(num)

print(c)