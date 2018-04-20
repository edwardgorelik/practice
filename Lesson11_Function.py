def get_integer(help_text="Give out your number now: "):
    return int(input(help_text))

def check_integer(number):
    yes = []
    test = range(1,number)

    for num in test:
        if number % num == 0:
            yes.append(num)

    if len(yes) > 2:
        print("Number is not Prime")
    else:
        print("Number is fuckin' Prime bro")

play = "y"

while play == "y":
    number = get_integer()
    check_integer(number)
    play = input("Another number?")