user = int(input("Give me a number, any number "))
check = int(input("Divide that number by what?"))

"""if user % 2 == 0:
    if user % 4 == 0:
        print("divisible by 4 too, nice")
    else:
        print("That was an even number")
elif user % 2 == 1:
    print("That was an odd number")
"""

if user % check == 0:
    print("perfect")
else:
    print("they've got a remainder")