import random
def createPassword(strength):
    list = ["big", "small", "happy", "dog", "cat", "animal", "good", "hello", "i", "we", "meow"]
    lower = [chr(x) for x in range(ord('a'), ord('z')+1)]
    upper = [chr(x) for x in range(ord('A'), ord('Z')+1)]
    number = range(0,9)
    special = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "=", "+", "<", ">", ",", ".", "/", "?", ";", ":", "|", "\\", "}", "\]", "\{", "[", "~", "`", "}" ]
    if strength == "yes":
        lowers = random.sample(lower, random.randint(1,5))
        uppers = random.sample(upper, random.randint(1,5))
        numbers = random.sample(number, random.randint(1,3))
        specials = random.sample(special, random.randint(1,2))
        password = lowers + uppers + numbers + specials
        random.shuffle(password)
        password = ''.join(''.join(str(elems) for elems in password))
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