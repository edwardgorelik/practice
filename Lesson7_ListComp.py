import random

a = random.sample(range(1000000),20)
even = [number for number in a if number % 2 == 0]

print(even)