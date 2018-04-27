import random
def createPassword(strength):
    password = []
    list = ["big", "small", "happy", "dog", "cat", "animal", "good", "hello", "i", "we", "meow"]
    if strength == "yes":
        password.append(random.sample("abcdefghijklmnopqrstuvwxyz", random.randint(1,5)))
        password.append(random.sample("ABCDEFGHIJKLMNOPQRSTUVWXYZ", random.randint(1,5)))
        password.append(random.sample("1234567890", random.randint(1,3)))
        password.append(random.sample("!@#$%^&*()<>,./?", random.randint(1,2)))
        random.shuffle(password)
        password = ''.join(''.join(elems) for elems in password)
        print(type(password))
    else:
        password.append(random.sample(list,random.randint(1,2)))
    return password

while True:
    strength = input("How strong do you want this password? (Yes/No only)")
    if strength.lower() != "yes" and strength.lower() != "no":
        print("Answer must be yes or no.")
        continue
    else:
        password = createPassword(strength)
        print(password)
        break